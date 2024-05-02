from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('meals/',views.meals_index, name='index'),
    path('meals/', views.MealList.as_view(), name='meals_index'),
    path('meals/create/', views.MealCreate.as_view(), name='meals_create'),
    path('meals/<int:pk>/', views.MealDetail.as_view(), name='meals_detail'),
    path('meals/<int:pk>/update/', views.MealUpdate.as_view(), name='meals_update'),
    path('meals/<int:pk>/delete/', views.MealDelete.as_view(), name='meals_delete'),
     ]