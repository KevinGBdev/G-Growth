from django.contrib import admin

from .models import Diagnostico, Pergunta, Resposta

admin.site.register(Pergunta)
admin.site.register(Diagnostico)
admin.site.register(Resposta)
