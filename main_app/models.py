from django.db import models
from django.urls import reverse
# Create your models here.

class Dolphin(models.Model):
  name = models.CharField(max_length=100)
  region = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  status = models.TextField(max_length=250)


  def __str__(self):
    return self.name

    # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'dolphin_id': self.id})
