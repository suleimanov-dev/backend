from django.core.validators import FileExtensionValidator
from django.db import models


class LinkType(models.Model):
    name = models.CharField(max_length=64)
    icon = models.FileField(
        upload_to='icons/links/',
        validators=[FileExtensionValidator(['svg'])],
        max_length=256
    )
