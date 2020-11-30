# Generated by Django 3.1.3 on 2020-11-24 11:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WorkWithProjects', '0002_remove_project_aurhors'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='aurhors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Authors'),
        ),
    ]
