from django.db import models

# Create your models here.

class Dolphin(models.Model):
  name = models.CharField(max_length=100)
  region = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  status = models.TextField(max_length=250)


  def __str__(self):
    return self.name

