from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def about(request):
    return render(request, 'core/about.html')

@login_required
def contact(request):
    return render(request, 'core/contact.html')

@login_required
def admin(request):
    return render(request, 'core/admin.html')

@login_required
def index(request):
    return render(request, 'core/base.html')