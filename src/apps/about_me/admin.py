from django.contrib import admin

from .models import MainInfo, ContactLink, TimelineElement, TimelineElementAttachment

# main_info.py
admin.site.register(MainInfo)
admin.site.register(ContactLink)

# timeline.py
admin.site.register(TimelineElement)
admin.site.register(TimelineElementAttachment)
