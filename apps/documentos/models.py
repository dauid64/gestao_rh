from django.db import models
from apps.funcionarios.models import Funcionario
from django.urls import reverse


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    dono = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def __str__(self):
        return self.descricao
    
    def get_absolute_url(self):
        return reverse('edit_funcionario', kwargs={'pk': self.dono.id})
