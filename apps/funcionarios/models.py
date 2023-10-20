from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.urls import reverse


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse("list_funcionarios")
    
