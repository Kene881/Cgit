# Generated by Django 3.1.3 on 2020-11-23 18:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='Description')),
                ('file', models.FileField(upload_to='', verbose_name='File_project')),
                ('aurhors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Authors')),
            ],
        ),
    ]
