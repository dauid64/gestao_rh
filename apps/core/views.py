from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.db.models import Sum
from .serializers import UserSerializer, GroupSerializer
from apps.registro_hora_extra.models import RegistroHoraExtra
from apps.departamentos.models import Departamento
from django.core import serializers
from django.http import HttpResponse
from .tasks import send_relatorio
from rest_framework import routers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@login_required
def home(request):
    usuario = request.user
    funcionario = request.user.funcionario
    return render(
        request,
        'core/index.html',
        context={
            'usuario': usuario,
            'total_funcionarios': funcionario.empresa.total_funcionarios,
            'total_funcionarios_ferias': funcionario.empresa.total_funcionarios_ferias,
            'total_funcionarios_doc_pendente': funcionario.empresa.total_funcionarios_doc_pendente,
            'total_hora_extra_pendente': RegistroHoraExtra.objects.filter(
                funcionario__empresa=funcionario.empresa, utilizada=False
            ).aggregate(Sum('horas'))['horas__sum'],
            'total_hora_extra_utilizadas': RegistroHoraExtra.objects.filter(
                funcionario__empresa=funcionario.empresa, utilizada=True
            ).aggregate(Sum('horas'))['horas__sum'],
        }
    )


def celery(request):
    send_relatorio.delay()
    return HttpResponse('Tarefa incluida na fila para execução')


def departamentos_ajax(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos_ajax.html', {'departamentos': departamentos})


def filtra_funcionarios(request):
    depart = request.GET['depart_id']
    departamento = Departamento.objects.get(id=depart)

    qs_json = serializers.serialize('json', departamento.funcionario_set.all())
    return HttpResponse(qs_json, content_type='application/json')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )