# Generated by Django 4.0.1 on 2022-01-22 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ('priority_number',)},
        ),
    ]
