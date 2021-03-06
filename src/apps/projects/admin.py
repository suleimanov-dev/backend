from django.contrib import admin

from .models import (
    Project, ProjectLink, ProjectArticle, Technology, ProjectTechnology, Instrument,
    ProjectInstrument, LinkType,
)

# technology.py
admin.site.register(Technology)

# instrument.py
admin.site.register(Instrument)

# link.py
admin.site.register(LinkType)

# project.py
admin.site.register(Project)
admin.site.register(ProjectLink)
admin.site.register(ProjectArticle)
admin.site.register(ProjectTechnology)
admin.site.register(ProjectInstrument)
