from django.urls import path
from movies import views

urlpatterns = [
    path('movies/', views.MovieList.as_view()),
    path('users/', views.UserList.as_view()),
]