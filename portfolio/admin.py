from typing import Tuple
from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Register your models here.

admin.site.register(Project, ProjectAdmin)