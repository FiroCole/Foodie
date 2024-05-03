from django.shortcuts import render, redirect
from .models import Meal, Comment, Location
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import CommentForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'home.html')
  
@login_required
def add_comment(request, pk):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.meal_id = meal_id
    new_comment.save()
  return redirect('meals_detail', meal_id=meal_id)

def assoc_location(request, meal_id, location_id):
  Meal.objects.get(id=meal_id).location.add(location_id)
  return redirect('meals_detail', meal_id=meal_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# CBV for Meals

class MealList(LoginRequiredMixin, ListView):
  model = Meal
  template_name = 'meal_list.html' 
  
  def get_queryset(self):
      return Meal.objects.filter(user=self.request.user)
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  # Assuming CommentForm is defined
        return context

class MealDetail(LoginRequiredMixin, DetailView):
    model = Meal

class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ['name', 'description']
    success_url = '/meals/{id}'
    
    def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)

class MealUpdate(LoginRequiredMixin, UpdateView):
    model = Meal
    fields = '__all__'
    

class MealDelete(LoginRequiredMixin, DeleteView):
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