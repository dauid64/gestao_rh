from typing import Any
from django.views.generic import ListView
from .models import RegistroHoraExtra
from apps.funcionarios.models import Funcionario


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return queryset