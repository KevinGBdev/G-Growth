from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    segmento = models.CharField(max_length=100)
    plano = models.CharField(
        max_length=20,
        choices=[
            ("gratuito", "Gratuito"),
            ("basico", "Básico"),
            ("pro", "Pro"),
        ],
    )

    def __str__(self) -> str:
        return f"{self.user.username} - {self.plano}"

