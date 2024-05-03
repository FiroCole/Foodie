from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    
    def __str__(self):
         return f'{self.city} ({self.id})'
         
class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.ManyToManyField(Location)
    image_url = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    # def get_absolute_url(self):
    #     return reverse('meals_detail', kwargs={'pk': self.pk})



    
class Comment(models.Model):
    user_commenting = models.CharField(max_length=200)
    date = models.DateField('Comment Date')
    comment =models.CharField(max_length=250)
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.get_comment_display()} on {self.date}"
  
    
    class Meta:
      ordering = ['-date']
