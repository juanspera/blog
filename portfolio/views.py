import datetime
from turtle import title

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

import django

from .forms import ProjectFormulario
from .models import Project

# Create your views here.

@login_required
def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects':projects})


@user_passes_test(lambda u: u.is_superuser)
def portfolio_formulario(request):

    if request.method == 'POST':
        mi_formulario = ProjectFormulario(request.POST, request.FILES)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            post = Project(title=data.get('title'), subtitle=data.get('subtitle'), description=data.get('description'), image=data.get('image'), link=data.get('link'))
            post.save()

            return redirect('portfolio')

    contexto = {
        'form': ProjectFormulario(),
        'titulo_form': 'Crear Post',
        'boton_envio': 'Crear'
    }

    return render(request, 'base_formulario.html', contexto)


@user_passes_test(lambda u: u.is_superuser)
def eliminar_portfolio(request, id):
    post_eliminar = Project.objects.get(id=id)
    post_eliminar.delete()

    messages.info(request, f"El post {post_eliminar} fue eliminado")

    return redirect('portfolio_admin')

@user_passes_test(lambda u: u.is_superuser)
def portfolio_admin(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio_admin.html', {'projects':projects})


@user_passes_test(lambda u: u.is_superuser)
def editar_portfolio(request, id):
    post_editar = Project.objects.get(id=id)

    if request.method == 'POST':
        mi_formulario = ProjectFormulario(request.POST, request.FILES)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            post_editar.title = data.get('title')
            post_editar.subtitle = data.get('subtitle')
            post_editar.description = data.get('description')
            post_editar.image = data.get('image')
            post_editar.link = data.get('link')
            try:
                post_editar.save()
            except django.db.utils.IntegrityError:
                messages.error(request, "La modificacion ha fallado")

            return redirect('portfolio_admin')

    contexto = {
        'form': ProjectFormulario(
            initial={
                "titulo": post_editar.title,
                "subtitulo": post_editar.subtitle,
                "comentario": post_editar.description
            }
        ),
        'titulo_form': 'Editar Post',
        'boton_envio': 'Editar'
    }

    return render(request, 'base_formulario.html', contexto)

