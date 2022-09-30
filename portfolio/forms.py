from datetime import date
from django import forms
from ckeditor.widgets import CKEditorWidget

class ProjectFormulario(forms.Form):
    title = forms.CharField(max_length=200, label='Título')
    subtitle = forms.CharField(max_length=200, label='Subtítulo',required=False)
    description = forms.CharField(label='Comentario', widget = CKEditorWidget())
    image = forms.ImageField(label='Imagen', required=False)
    link = forms.URLField(required=False, label="Link")

class BusquedaPostForm(forms.Form):
    title = forms.CharField(max_length=200, label="Título")