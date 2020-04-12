from django.urls import path
from movies import views

urlpatterns = [
    path('movies/', views.MovieList),
    path('movies/<int:pk>/', views.MovieDetail),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]