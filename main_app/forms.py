from django.forms import ModelForm
from .models import Comment, Location

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['date', 'user_commenting', 'comment']
    
class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['city', 'country']  # Make sure to include 'country' if it's part of the Location model
