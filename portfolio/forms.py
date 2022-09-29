from django import forms


class ProjectFormulario(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField()
    