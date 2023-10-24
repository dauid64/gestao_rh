from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraBaseEdit,
    HoraExtraDelete,
    HoraExtraCreate,
    UtilizouHoraExtra,
    NaoUtilizouHoraExtra
)
from django.urls import path

urlpatterns = [
    path(
        '',
        HoraExtraList.as_view(),
        name='list_hora_extra'
    ),
    path(
        'novo/',
        HoraExtraCreate.as_view(),
        name='create_hora_extra'
    ),
    path(
        'editar-funcionario/<int:pk>',
        HoraExtraEdit.as_view(),
        name='edit_hora_extra'
    ),
    path(
        'editar/<int:pk>',
        HoraExtraBaseEdit.as_view(),
        name='edit_hora_extra_base'
    ),
    path(
        'utilizou-hora-extra/<int:pk>',
        UtilizouHoraExtra.as_view(),
        name='utilizou_hora_extra'
    ),
    path(
        'nao-utilizou-hora-extra/<int:pk>',
        NaoUtilizouHoraExtra.as_view(),
        name='nao_utilizou_hora_extra'
    ),
    path(
        'deletar/<int:pk>',
        HoraExtraDelete.as_view(),
        name='delete_hora_extra'
    ),
]
