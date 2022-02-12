from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=64, unique=True)
    icon = models.ImageField(upload_to='icons/technologies/', max_length=256)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
