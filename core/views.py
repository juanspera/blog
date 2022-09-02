from django.shortcuts import render

# Create your views here.
def portfolio(request):
    return render(request, 'core/portfolio.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')