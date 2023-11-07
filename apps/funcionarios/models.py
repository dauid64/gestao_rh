from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.db.models import Sum
from django.urls import reverse


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, null=True, blank=True
    )
    de_ferias = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    @property
    def total_horas_extra(self):
        total = self.registrohoraextra_set.filter(
            utilizada=False
        ).aggregate(
            Sum('horas'))['horas__sum']
        return total or 0

    def get_absolute_url(self):
        return reverse("list_funcionarios")
