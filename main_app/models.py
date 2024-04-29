from django.db import models
from django.urls import reverse

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={
            'meal_id': self.id
        })

class Comment(models.Model):
    user = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.user} ({self.id})'
    
