from django.urls import path
from . import views

urlpatterns = [
    path('modulos/', views.listar_modulos, name='listar_modulos'),
]
