from django.core.validators import FileExtensionValidator
from django.db import models

from ..validators import validate_contact_link
from ...helpers.models import SingletonModel


class MainInfo(SingletonModel):
    name = models.CharField(max_length=64, default='')
    location = models.CharField(max_length=64, default='')
    portrait = models.ImageField(
        upload_to='images/portraits/',
        max_length=256,
        blank=True,
        null=True
    )
    resume_file = models.FileField(
        upload_to='files/resumes/',
        validators=[FileExtensionValidator(['pdf', 'doc'])],
        max_length=256,
        blank=True,
        null=True
    )

    def __str__(self):
        return 'Main info'


class ContactLink(models.Model):
    name = models.CharField(max_length=64)
    icon = models.FileField(
        upload_to='icons/contact_links/',
        validators=[FileExtensionValidator(['svg'])],
        max_length=256
    )
    link = models.CharField(max_length=256, validators=[validate_contact_link])
    priority_number = models.IntegerField(default=0)

    class Meta:
        ordering = ('-priority_number',)

    def __str__(self):
        return self.name


class TechnologyBlock(models.Model):
    class Type(models.TextChoices):
        backend = 'BACKEND', 'backend'
        db = 'DB', 'DB'
        frontend = 'FRONTEND', 'frontend'
        design = 'DESIGN', 'design'
        other = 'OTHER', 'other'

    content = models.TextField(max_length=512)
    type = models.CharField(max_length=32, choices=Type.choices, unique=True)
    priority_number = models.IntegerField(default=0)

    class Meta:
        ordering = ('-priority_number',)

    def __str__(self):
        return self.type
