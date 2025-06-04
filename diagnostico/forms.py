from django import forms
from .models import Pergunta


class DiagnosticoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        perguntas = kwargs.pop('perguntas')
        super().__init__(*args, **kwargs)
        for pergunta in perguntas:
            self.fields[f'pergunta_{pergunta.id}'] = forms.CharField(
                label=pergunta.texto,
                widget=forms.TextInput(attrs={'class': 'form-control'}),
                required=True,
            )
