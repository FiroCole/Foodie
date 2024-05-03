from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['date', 'user_commenting', 'comment']
    
class LocationForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['', 'user_commenting', 'comment']