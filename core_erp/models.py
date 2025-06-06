from django.db import models
from django.contrib.auth import get_user_model


class BaseERPModel(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
