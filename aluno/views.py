from django.shortcuts import render
from django.contrib import messages
from aluno.form import AlunoFormModel
from aluno.models import Aluno


def index_aluno(request):
    aluno_sql = Aluno.objects.all()
    context = {
        'aluno': aluno_sql
    }

    return render(request, 'aluno/index.html', context)


def cadastro_aluno(request):
    if str(request.method) == 'POST':
        aluno = AlunoFormModel(request.POST)
        if aluno.is_valid():
            aluno.save()
            messages.success(request, 'Legal')
        else:
            messages.error(request, 'Erro ao salvar')
    else:
        aluno = AlunoFormModel()
    context = {
        'form': aluno
    }

    return render(request, 'aluno/form_cadastro.html', context)
