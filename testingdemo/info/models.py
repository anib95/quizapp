from __future__ import unicode_literals

from django.db import models


# Create your models here.

class person(models.Model):
    name=models.CharField(max_length=100)
    marks=models.IntegerField()
    salary=models.IntegerField()
    photo=models.CharField(max_length=100)

