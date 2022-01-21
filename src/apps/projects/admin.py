from django.contrib import admin

from .models import (
    Project, ProjectLink, ProjectArticle, Technology, ProjectTechnology, Instrument,
    ProjectInstrument,
)

admin.site.register(Project)
admin.site.register(ProjectLink)
admin.site.register(ProjectArticle)
admin.site.register(Technology)
admin.site.register(ProjectTechnology)
admin.site.register(Instrument)
admin.site.register(ProjectInstrument)
