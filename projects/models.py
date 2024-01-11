from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    technology = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)