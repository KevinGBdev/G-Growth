from django.db import models
from django.contrib.auth import get_user_model


class ModuloAtivo(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nome_modulo = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('usuario', 'nome_modulo')

    def __str__(self) -> str:
        return f"{self.usuario.username} - {self.nome_modulo}" 
