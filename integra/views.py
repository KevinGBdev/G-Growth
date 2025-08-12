from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ModuloAtivo


@login_required
def listar_modulos(request):
    modulos = ModuloAtivo.objects.filter(usuario=request.user)
    return render(request, 'integra/modulos.html', {'modulos': modulos})
