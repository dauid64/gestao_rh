from .views import ( 
    FuncionariosList, 
    FuncionarioEdit, 
    FuncionarioDelete, 
    FuncionarioCreate 
)
from django.urls import path

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name='edit_funcionario'),
    path('deletar/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
]
