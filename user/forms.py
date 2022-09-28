from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import Avatar


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = "__all__"


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'email', 'last_name')
