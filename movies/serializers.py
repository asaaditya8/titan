from rest_framework import serializers
from .models import movies


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = movies
        fields = '__all__'
