from django.core.validators import FileExtensionValidator
from django.db import models

from src.apps.common.models import SingletonModel


class MainInfo(SingletonModel):
    name = models.CharField(max_length=64, default='John Doe')
    job = models.CharField(max_length=64, default='meme-creator')
    location = models.CharField(max_length=64, default='Los Santos, USA')
    resume_file = models.FileField(
        upload_to='resume_files/',
        validators=[FileExtensionValidator(['pdf', 'doc'])],
        max_length=256,
        blank=True,
        null=True
    )


class ContactLink(models.Model):
    name = models.CharField(max_length=64)
    icon = models.FileField(
        upload_to='contact_link_icons/',
        validators=[FileExtensionValidator(['svg'])],
        max_length=256
    )
    link = models.CharField(max_length=256)
