from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
    View
)
from .models import Funcionario
from django.contrib.auth.models import User
import io
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.usuario = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)


def relatorio_funcionarios(request):
    response = HttpResponse(content='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(250, 810, "Relatório de funcionários")
    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

    str_ = "Nome: %s | Hora Extra: %2.f"
    y = 790
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (funcionario.nome, funcionario.total_horas_extra ))
        y -= 20

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode('UTF-8')), response
        )
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf'
            )
            response['Content-Disposition'] = 'attachment; filenmae=%s.pdf' % filename
            return response
        else:
            return HttpResponse('Error Rendering PDF', status=400)
        

class RelatorioFuncionariosHtml(View):
    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')