from __future__ import unicode_literals

from django.db import models

# Create your models here.
class quiz(models.Model):
    question=models.CharField(max_length=1000)
    option1=models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    correct = models.IntegerField()