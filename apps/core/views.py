from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer
from .tasks import send_relatorio
from rest_framework import routers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@login_required
def home(request):
    usuario = request.user
    return render(
        request,
        'core/index.html',
        context={
            'usuario': usuario
        }
    )


def celery(request):
    send_relatorio.delay()
    return HttpResponse('Tarefa incluida na fila para execução')


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