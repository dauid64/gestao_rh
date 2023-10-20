from .views import (
    DepartamentosList,
    DepartamentoCreate,
    DepartamentoEdit,
    DepartamentoDelete
)
from django.urls import path

urlpatterns = [
    path('', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo', DepartamentoCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>', DepartamentoEdit.as_view(), name='edit_departamento'),
    path('deletar/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamento'),
]
