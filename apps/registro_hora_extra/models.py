from django.db import models
from apps.funcionarios.models import Funcionario
from django.urls import reverse


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    horas = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return reverse('edit_hora_extra', kwargs={"pk": self.id})

    def __str__(self):
        return self.motivo
