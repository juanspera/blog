from django.urls import path
from . import views

urlpatterns = [
     path('blog/',views.portfolio, name='portfolio'),
     path('crear_post/', views.portfolio_formulario, name='PortfolioFormulario'),
]




   