from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=30, null=False)
    date = models.DateField(null=False)
    owner = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.title