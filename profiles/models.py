from django.db import models

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True)
    name = models.CharField(max_length=120)


