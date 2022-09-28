from msilib.schema import Class
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo',null=True, blank=True)
    description = RichTextField(verbose_name='Comentario')
    image = models.ImageField(verbose_name='Imagen', upload_to="Blog", null=True, blank=True)
    link = models.URLField(null=True, blank=True, verbose_name="Link")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ["-created"]
    
    def __str__(self):
        return self.title
