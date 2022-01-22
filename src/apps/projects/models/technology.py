from django.db import models


class Technology(models.Model):
    class TechnologyType(models.TextChoices):
        backend = 'BACKEND', 'backend'
        db = 'DB', 'DB'
        frontend = 'FRONTEND', 'frontend'
        design = 'DESIGN', 'design'
        other = 'OTHER', 'other'

    name = models.CharField(max_length=64, unique=True)
    icon = models.ImageField(upload_to='icons/technologies/', max_length=256)
    type = models.CharField(max_length=32, choices=TechnologyType.choices)
    is_shown_in_resume = models.BooleanField(default=False)
    priority_number = models.IntegerField(default=0)


class TechnologyPair(models.Model):
    obj = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='technology_pair_obj_1')
    pair = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='technology_pair_obj_2')


class TechnologySubstitute(models.Model):
    obj = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='technology_substitute_obj_1')
    substitute = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='technology_substitute_obj_2')
