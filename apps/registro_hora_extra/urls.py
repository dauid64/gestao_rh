from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraDelete,
    HoraExtraCreate
)
from django.urls import path

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo/', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='edit_hora_extra'),
    path('deletar/<int:pk>', HoraExtraDelete.as_view(), name='delete_hora_extra'),
]
