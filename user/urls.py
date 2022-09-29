from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import *

urlpatterns = [
    path('login/', login_request, name='UserLogin'),
    path('registro/', register, name='UserRegister'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='UserLogout'),
    path('editar/', editar_usuario, name='UserEditar'),
    path('avatar/', upload_avatar, name='UserAvatar'),
    path('prueba/', prueba, name='prueba'),
]
