from django.shortcuts import render, redirect
from .models import Meal, Comment, Location
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import CommentForm, LocationForm
from django.urls import reverse
from django.shortcuts import get_object_or_404

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
        meal = Meal.objects.get(pk=pk)  # Get the meal object
        new_comment.meal = meal  # Set the meal of the comment correctly
        new_comment.save()
        return redirect('meals_detail', pk=pk)

@login_required
def add_location(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save()
            meal.location.add(location)  # Adds the location to the meal
            return redirect('meals_detail', pk=pk)
    else:
        form = LocationForm()
    return render(request, 'add_location.html', {'form': form, 'meal': meal})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('meals_index')
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
   

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a CommentForm
        context['comment_form'] = CommentForm()
        context['location_form'] = LocationForm()
        return context

class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ['name', 'description']
    success_url = '/meals/{id}'
    
    def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)

class MealUpdate(LoginRequiredMixin, UpdateView):
    model = Meal
    fields = ['name', 'description']
    success_url = '/meals/{id}'

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

    def form_valid(self, form):
        # Get the meal using the meal_id passed in the URL or form
        meal_id = self.kwargs.get('meal_id')  # Assuming you're capturing 'meal_id' from the URL
        meal = get_object_or_404(Meal, pk=meal_id)
        form.instance.meal = meal  # Set the meal of the comment to the meal fetched
        return super().form_valid(form)

    def get_success_url(self):
        # Redirects to the meal detail page after the comment is successfully created
        meal_id = self.kwargs.get('meal_id')
        return reverse('meals_detail', kwargs={'pk': meal_id})  # Adjust 'meals_detail' to your URL name and kwargs accordingly

    
class CommentUpdate(UpdateView):
    model = Comment
    fields = '__all__'

class CommentDelete(DeleteView):
    model = Comment
    success_url = '/comments'
    





def assoc_comment(request, meal_id, comment_id):
  Meal.objects.get(id=meal_id).comments.add(comment_id)
  return redirect('detail', meal_id=meal_id)