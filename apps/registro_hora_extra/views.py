from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, View
from django.http import HttpResponse
from apps.funcionarios.models import Funcionario
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm
import csv
import xlwt


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return queryset


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraBaseEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_success_url(self):
        return reverse_lazy('edit_hora_extra_base', kwargs={'pk': self.object.id})

    def get_form_kwargs(self):
        kwargs = super(HoraExtraBaseEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        funcionario = Funcionario.objects.get(id=self.request.POST['funcionario_id'])

        return JsonResponse(
            data={
                'message': 'Requisicao executada',
                'horas': funcionario.total_horas_extra
            }
        )


class NaoUtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = False
        registro_hora_extra.save()

        funcionario = Funcionario.objects.get(id=self.request.POST['funcionario_id'])

        return JsonResponse(
            data={
                'message': 'Requisicao executada',
                'horas': funcionario.total_horas_extra
            }
        )


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="myfile.csv"'

        empresa_logada = request.user.funcionario.empresa
        registro_he = RegistroHoraExtra.objects.filter(
            utilizada=False,
            funcionario__empresa=empresa_logada
        )

        writer = csv.writer(response)
        writer.writerow(['id', 'Motivo', 'Funcionário', 'Rest. func', 'Horas'])
        for registro in registro_he:
            writer.writerow([
                registro.id, registro.motivo, registro.funcionario, 
                registro.funcionario.total_horas_extra, registro.horas
            ])

        return response


class ExportarExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="relatorio.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Motivo', 'Funcionario', 'Rest. Func', 'Horas']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        empresa_logada = request.user.funcionario.empresa
        registros = RegistroHoraExtra.objects.filter(
            utilizada=False,
            funcionario__empresa=empresa_logada
        )

        row_num = 1
        for registro in registros:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.motivo, font_style)
            ws.write(row_num, 2, registro.funcionario.nome, font_style)
            ws.write(row_num, 3, registro.funcionario.total_horas_extra, font_style)
            ws.write(row_num, 4, registro.horas, font_style)
            row_num += 1
        
        wb.save(response)
        return response

