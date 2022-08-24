from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import render, redirect


def index_home(request):
    return render(
        request, 'home/index.html'
    )


def cadastro_usuario(request):
    if str(request.method) != 'POST':
     return render(request, 'home/usuario.html')
    else:
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        primeiro_nome = request.POST.get('primeiro')
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')

    try:
        validate_email(email)
    except:
        messages.error(request, 'email inválido')
        return render(request, 'home/usuario.html')

    if User.object.filter(email=email).exists():
        messages.error(request, 'email já existe ')
        return render(request, 'home/usuario.html')

    if User.object.filter(username=usuario).exists():
        messages.error(request, 'usuario já existe ')
        return render(request, 'home/usuario.html')

    if len(senha1) < 6:
        messages.error(request, 'usuario já existe')
        return render(request, 'home/usuario.html')

    if senha1 != senha2:
            messages.error(request, 'senha diferente')
            return render(request, 'home/usuario.html')
    usuario_correto = User.objects.create_user(
        username=usuario,
        email=email,
        first_name=primeiro_nome,
        password=senha1,
    )
    usuario_correto.save()
    return render(request, 'home/login.html')

def login_usuario(request):
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha1')
    user = auth.authenticate(
        request,
        username=usuario,
        password=senha
    )
    if user:
        auth.login(request, user)
        return redirect('index_home')

    else:
        messages.error(request,
        'usuário  ou senha inválida, se errar de novo já sabe hehe')

    return render(request, 'home/login.html')