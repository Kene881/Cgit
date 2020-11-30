from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name = 'Name', max_length=50, blank = True)
    description = models.TextField(verbose_name = 'Description', max_length=255, blank=True)
    file = models.FileField(verbose_name='File_project')
    authors = models.ManyToManyField(User, verbose_name='Authors')