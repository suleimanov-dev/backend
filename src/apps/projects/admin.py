from django.contrib import admin

from src.apps.projects.models import Project, ProjectLink, ProjectArticle, Technology, ProjectTechnology

admin.site.register(Project)
admin.site.register(ProjectLink)
admin.site.register(ProjectArticle)
admin.site.register(Technology)
admin.site.register(ProjectTechnology)
