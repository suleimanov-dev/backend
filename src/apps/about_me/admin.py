from django.contrib import admin

from .models import (
    MainInfo, ContactLink, TimelineElement, TimelineElementAttachment, TechnologyBlock
)

# main_info.py
admin.site.register(MainInfo)
admin.site.register(ContactLink)
admin.site.register(TechnologyBlock)

# timeline.py
admin.site.register(TimelineElement)
admin.site.register(TimelineElementAttachment)
