from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'title', 'date']


class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'movies']