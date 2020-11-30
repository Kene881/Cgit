from django.db import models
from django.contrib.auth.models import User
from WorkWithProjects.models import Project

# Create your models here.
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Content')