from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('panel/',views.panel, name='panel'),
    path('index/',views.index, name='index'),
]
