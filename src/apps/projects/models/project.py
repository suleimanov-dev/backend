from django.core.validators import FileExtensionValidator
from django.db import models

from .instrument import Instrument
from .link import LinkType
from .technology import Technology


class Project(models.Model):
    class Involvement(models.TextChoices):
        individual = 'INDIVIDUAL', 'Individual'
        group = 'GROUP', 'Group'

    class Designation(models.TextChoices):
        commercial = 'COMMERCIAL', 'Commercial'
        personal = 'PERSONAL', 'Personal'
        study = 'STUDY', 'Study'

    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='icons/projects/', max_length=256)
    date_created = models.DateField()
    involvement = models.CharField(max_length=32, choices=Involvement.choices)
    designation = models.CharField(max_length=32, choices=Designation.choices)
    overview_video = models.FileField(
        upload_to='videos/overviews/',
        validators=[FileExtensionValidator(['mp4'])],
        max_length=256,
        blank=True,
        null=True
    )
    is_actual = models.BooleanField(default=False)


class ProjectLink(models.Model):
    link = models.URLField(max_length=256)
    link_type = models.ForeignKey(LinkType, on_delete=models.RESTRICT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectArticle(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectTechnology(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.RESTRICT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectInstrument(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.RESTRICT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
