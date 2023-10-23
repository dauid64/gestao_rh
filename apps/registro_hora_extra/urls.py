from .views import ( 
    HoraExtraList
)
from django.urls import path

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    # path('novo/', FuncionarioCreate.as_view(), name='create_funcionario'),
    # path('editar/<int:pk>', FuncionarioEdit.as_view(), name='edit_funcionario'),
    # path('deletar/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
]
