from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer
from rest_framework import routers, viewsets


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer