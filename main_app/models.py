from django.db import models
from django.urls import reverse
# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

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

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    choices = MEALS, 
    default=MEALS[0][0])

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
    
  dolphin = models.ForeignKey(
    Dolphin, 
    on_delete=models.CASCADE
    )

  class Meta:
    ordering = ['-date']