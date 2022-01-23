from django.db import models
from tinymce import models as tinymce_models


class TimelineElement(models.Model):
    start_year = models.DateField()
    end_year = models.DateField(blank=True, null=True)
    content = tinymce_models.HTMLField(max_length=1024)

    class Meta:
        ordering = ('-start_year', '-end_year')


class TimelineElementAttachment(models.Model):
    attachment = models.ImageField(upload_to='images/timeline_attachments/', max_length=256)
    element = models.ForeignKey(TimelineElement, on_delete=models.CASCADE)
