from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

import django

from user.forms import UserRegisterForm, AvatarForm
from user.models import Avatar

@login_required
def upload_avatar(request):
    usuario = request.user.id
    if request.method == "POST":
        
        formulario = AvatarForm(request.POST, request.FILES)
        
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(username_id=usuario)
            
            if  len(avatar) > 0:
                avatar = Avatar.objects.get(username_id=usuario)
                avatar.delete()
                avatar = Avatar(username_id=usuario, imagen=data.get("imagen"))
                avatar.save()

            else:
                avatar = Avatar(username_id=usuario, imagen=data.get("imagen"))
                avatar.save()            

        return redirect('portfolio')

    contexto = {
        "form": AvatarForm(
            
            ),
        'boton_envio': 'Subir'
    }
    return render(request, "base_formulario.html", contexto)


@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            usuario.username = data.get('username')
            usuario.email = data.get('email')
            usuario.last_name = data.get('last_name')

            usuario.save()

            messages.info(request, 'Tu usuario fue modificado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no puso ser modificado!')
        return redirect('portfolio')
    contexto = {
        # 'form': UserCreationForm(),
        'form': UserRegisterForm(
            initial={
                'username': usuario.username,
                'email': usuario.email,
                'last_name': usuario.last_name
            }),
            'titulo_form': 'Editar Usuario',
        'boton_envio': 'Editar',
    }

    return render(request, 'base_formulario.html', contexto)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')

            else:
                messages.info(request, 'Por favor verificar usuario o contrasenia!')
        else:
            messages.info(request, 'inicio de sesion fallido!')

        return redirect('portfolio')

    contexto = {
        'form': AuthenticationForm(),
        'titulo_form': 'Login',
        'boton_envio': 'Enviar'
    }
    return render(request, 'base_formulario.html', contexto)


def register(request):
    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no puso ser registrado!')
        return redirect('portfolio')

    contexto = {
        # 'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'titulo_form': 'Registrarse',
        'boton_envio': 'Enviar'
    }

    return render(request, 'base_formulario.html', contexto)


def prueba(request):
    return render(request, 'core/base.html')