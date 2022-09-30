from django.urls import path
from . import views

urlpatterns = [
     path('blog/',views.portfolio, name='portfolio'),
     path('crear_post/', views.portfolio_formulario, name='PortfolioFormulario'),
     path('eliminar_post/<int:id>', views.eliminar_portfolio, name='EliminarPost'),
     path('blog_admin/',views.portfolio_admin, name='portfolio_admin'),
     path('editar_post/<int:id>', views.editar_portfolio, name='EditarPost'),
     path('buscar_post/', views.busqueda_post, name='BuscarPost'),
     path('busqueda_post_res/', views.busqueda_post_res, name='BuscarPostRes'),
]




   