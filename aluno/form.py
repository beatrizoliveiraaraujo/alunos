from django import forms
from aluno.models import Aluno


class AlunoFormModel(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'telefone']
