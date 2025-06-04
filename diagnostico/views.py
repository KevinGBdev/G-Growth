from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import DiagnosticoForm
from .models import Diagnostico, Pergunta, Resposta


@login_required
def responder_diagnostico(request):
    perguntas = Pergunta.objects.order_by('ordem')

    if request.method == 'POST':
        form = DiagnosticoForm(request.POST, perguntas=perguntas)
        if form.is_valid():
            diag = Diagnostico.objects.create(usuario=request.user)
            for pergunta in perguntas:
                resposta_texto = form.cleaned_data.get(f'pergunta_{pergunta.id}')
                Resposta.objects.create(
                    diagnostico=diag,
                    pergunta=pergunta,
                    resposta=resposta_texto,
                )
            return redirect('resultado_diagnostico', diag.id)
    else:
        form = DiagnosticoForm(perguntas=perguntas)

    return render(request, 'diagnostico/responder.html', {'form': form})


@login_required
def resultado_diagnostico(request, id):
    diagnostico = get_object_or_404(Diagnostico, id=id, usuario=request.user)
    respostas = Resposta.objects.filter(diagnostico=diagnostico)

    alertas = []
    for r in respostas:
        if 'não' in r.resposta.lower():
            alertas.append(f'Atenção à resposta negativa em: "{r.pergunta.texto}"')

    context = {
        'diagnostico': diagnostico,
        'respostas': respostas,
        'alertas': alertas,
    }
    return render(request, 'diagnostico/resultado.html', context)
