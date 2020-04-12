from django.conf import settings
from django.shortcuts import render
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework import generics, permissions, filters
from rest_framework.authtoken.models import Token

# Create your views here.
from .models import Movie
from .permissions import IsOwnerOrReadOnly
from .serializers import MoviesSerializer, UserSerializer


class MovieList(generics.ListCreateAPIView):
    serializer_class = MoviesSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]
    ordering_fields = ['title', 'date']
    ordering = ['title']
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        search = self.request.query_params.get('search', None)
        sort = self.request.query_params.get('sort', None)
        if search is not None:
            queryset = Movie.objects.all()
        else:
            queryset = Movie.objects.filter(owner=user)
            if sort is not None:
                queryset = queryset.order_by(sort)
            else:
                queryset = queryset.order_by('title')

        return queryset


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
