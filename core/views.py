from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def users(request):
    return render(request, 'core/users.html')

def index(request):
    return render(request, 'core/base.html')