from django import forms
from django.forms import widgets

# models
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ["titulo", "tarefa"]
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nova Tarefa'}))