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

            curso1 = Project(title=data.get('title'), subtitle=data.get('subtitle'), description=data.get('description'), image=data.get('image'), link=data.get('link'))
            curso1.save()

            return redirect('portfolio')

    contexto = {
        'form': ProjectFormulario(),
        'titulo_form': 'Crear Post',
        'boton_envio': 'Crear'
    }

    return render(request, 'base_formulario.html', contexto)