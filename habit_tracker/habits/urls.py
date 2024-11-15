from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_habit, name='add_habit'),
    path('track/<int:habit_id>/', views.track_progress, name='track_progress'),
]
