from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

@login_required
def about(request):
    return render(request, 'core/about.html')

@login_required
def contact(request):
    return render(request, 'core/contact.html')

@user_passes_test(lambda u: u.is_superuser)
def panel(request):
    return render(request, 'core/panel.html')

@login_required
def index(request):
    return render(request, 'core/base.html')