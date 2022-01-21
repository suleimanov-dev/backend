from django.contrib import admin

from src.apps.projects.models import Project, ProjectLink

admin.site.register(Project)
admin.site.register(ProjectLink)
