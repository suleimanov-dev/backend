# Generated by Django 4.0.1 on 2022-01-23 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0003_technology_alter_contactlink_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechnologySubstitute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technology_substitute_obj_1', to='about_me.technology')),
                ('obj_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technology_substitute_obj_2', to='about_me.technology')),
            ],
        ),
        migrations.CreateModel(
            name='TechnologyPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technology_pair_obj_1', to='about_me.technology')),
                ('obj_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technology_pair_obj_2', to='about_me.technology')),
            ],
        ),
    ]