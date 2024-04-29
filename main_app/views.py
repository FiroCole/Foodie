from django.shortcuts import render

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return(request, 'about.html')

def meals_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'meals/index.html', {
    'meals': meals
  })