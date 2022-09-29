from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('admin/',views.admin, name='admin'),
    path('index/',views.index, name='index'),
]
