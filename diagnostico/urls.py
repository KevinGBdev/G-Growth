from django.urls import path

from . import views

urlpatterns = [
    path('responder/', views.responder_diagnostico, name='responder_diagnostico'),
    path('resultado/<int:id>/', views.resultado_diagnostico, name='resultado_diagnostico'),
]
