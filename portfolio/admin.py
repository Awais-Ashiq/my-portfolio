from django.contrib import admin
from .models import Project
from blog.models import newProject

admin.site.register(Project)
admin.site.register(newProject)
