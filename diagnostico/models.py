from django.db import models
from django.contrib.auth.models import User


class Pergunta(models.Model):
    texto = models.TextField()
    segmento = models.CharField(max_length=100, blank=True)
    ordem = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.ordem}. {self.texto[:50]}"


class Diagnostico(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Diagnóstico de {self.usuario.username} em {self.criado_em:%d/%m/%Y}"


class Resposta(models.Model):
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.pergunta.texto[:30]} - {self.resposta}"
