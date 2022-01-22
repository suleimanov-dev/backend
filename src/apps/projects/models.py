from django.db import models


class Project(models.Model):
    class Involvement(models.TextChoices):
        individual = 'INDIVIDUAL', 'Individual'
        group = 'GROUP', 'Group'

    class Designation(models.TextChoices):
        commercial = 'COMMERCIAL', 'Commercial'
        personal = 'PERSONAL', 'Personal'
        study = 'STUDY', 'Study'

    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='project_icons/', max_length=256)
    date_created = models.DateField()
    involvement = models.CharField(
        max_length=10,
        choices=Involvement.choices
    )
    designation = models.CharField(
        max_length=10,
        choices=Designation.choices
    )
    overview_video = models.FileField(upload_to='project_overview_videos/', max_length=256, blank=True, null=True)
    is_actual = models.BooleanField(default=False)


class ProjectLink(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='project_link_icons/', max_length=256)
    link = models.CharField(max_length=256)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectArticle(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Technology(models.Model):
    name = models.CharField(max_length=64, unique=True)
    icon = models.ImageField(upload_to='technology_icons/', max_length=256)


class ProjectTechnology(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.RESTRICT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Instrument(models.Model):
    name = models.CharField(max_length=64, unique=True)
    icon = models.ImageField(upload_to='instrument_icons/', max_length=256)


class ProjectInstrument(models.Model):
    technology = models.ForeignKey(Instrument, on_delete=models.RESTRICT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
