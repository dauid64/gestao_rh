from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    usuario = request.user
    return render(
        request,
        'core/index.html',
        context={
            'usuario': usuario
        }
    )
