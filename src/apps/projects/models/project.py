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

    name = models.CharField(max_length=64, unique=True)
    icon = models.ImageField(upload_to='icons/projects/', max_length=256)
    month_created = models.DateField()
    involvement = models.CharField(max_length=32, choices=Involvement.choices)
    designation = models.CharField(max_length=32, choices=Designation.choices)
    short_description = models.TextField(max_length=512)
    overview_video = models.FileField(
        upload_to='videos/overviews/',
        validators=[FileExtensionValidator(['mov', 'mp4'])],
        max_length=256,
        blank=True,
        null=True
    )
    overview_video_preview = models.ImageField(
        upload_to='images/overview_previews/',
        max_length=256,
        blank=True,
        null=True
    )
    is_actual = models.BooleanField(default=False)
    is_shown = models.BooleanField(default=False)

    class Meta:
        ordering = ('-month_created',)

    def __str__(self):
        return self.name


class ProjectLink(models.Model):
    link = models.URLField(max_length=256)
    link_type = models.ForeignKey(LinkType, on_delete=models.RESTRICT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project} {self.link_type}'


class ProjectArticle(models.Model):
    class Title(models.TextChoices):
        description = 'DESCRIPTION', 'Description'
        features = 'FEATURES', 'Features'
        contribution = 'CONTRIBUTION', 'Contribution'

    title = models.CharField(max_length=64, choices=Title.choices)
    text = models.TextField(max_length=2048)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project} {self.title}'


class ProjectTechnology(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.RESTRICT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project} {self.technology}'


class ProjectInstrument(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.RESTRICT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project} {self.instrument}'
