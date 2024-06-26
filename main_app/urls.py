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
    path('meals/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('meals/<int:pk>/add_location/', views.add_location, name='add_location'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/logout/', views.user_logout, name='user_logout'),
    path('meals/<int:meal_id>/add_comment/', views.CommentCreate.as_view(), name='add_comment'),
     ]