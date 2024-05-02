from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Location(models.Model):
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    
    def __str__(self):
         return f'{self.city} ({self.id})'
         
class Meal(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.ManyToManyField(Location)
    image_url = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('meals_detail', kwargs={'pk': self.pk})



    
class Comment(models.Model):
    user_commenting = models.CharField(max_length=200)
    comment =models.CharField(max_length=250)
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user} ({self.id})'
    
