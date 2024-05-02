from django.shortcuts import render, redirect
from .models import Meal, Comment, User, Location
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def meals_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'meals/index.html', {
    'meals': meals
  })

# CBV for Meals
class MealList(ListView):
  model = Meal

class MealDetail(DetailView):
    model = Meal

class MealCreate(CreateView):
    model = Meal
    fields = '__all__'

class MealUpdate(UpdateView):
    model = Meal
    fields = '__all__'

class MealDelete(DeleteView):
    model = Meal
    success_url = '/meals'

# CBV for Comments
class CommentList(ListView):
  model = Comment

class CommentDetail(DetailView):
    model = Comment

class CommentCreate(CreateView):
    model = Comment
    fields = '__all__'

class CommentUpdate(UpdateView):
    model = Comment
    fields = '__all__'

class CommentDelete(DeleteView):
    model = Comment
    success_url = '/comments'
    





def assoc_comment(request, meal_id, comment_id):
  Meal.objects.get(id=meal_id).comments.add(comment_id)
  return redirect('detail', meal_id=meal_id)