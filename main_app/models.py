from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Dolphin(models.Model):
  name = models.CharField(max_length=100)
  region = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  status = models.TextField(max_length=250)
  toys = models.ManyToManyField(Toy)



  def __str__(self):
    return self.name

    # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'dolphin_id': self.id})

  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS) 

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