from django.contrib import admin

from src.apps.projects.models import Project, ProjectLink, ProjectArticle

admin.site.register(Project)
admin.site.register(ProjectLink)
admin.site.register(ProjectArticle)
