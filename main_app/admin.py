from django.contrib import admin
from .models import Comment, Location, Meal, User

# Register your models here.
admin.site.register(Comment)
admin.site.register(Location)
admin.site.register(Meal)
admin.site.register(User)