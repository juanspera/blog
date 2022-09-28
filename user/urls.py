from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import *

urlpatterns = [
    path('login/', login_request, name='UserLogin'),
    path('registro/', register, name='UserRegister'),
    path('logout/', LogoutView.as_view(template_name='user/templates/logout.html'), name='CoderLogout'),
    path('editar/', editar_usuario, name='UserEditar'),
    path('avatar/', upload_avatar, name='UserAvatar'),
]
