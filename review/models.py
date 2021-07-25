from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Cast(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    birthdate = models.DateField()
    best_work = models.CharField(max_length=300)
    achievements = models.TextField()
    cast_image = models.ImageField(default='default.jpg', upload_to='review/static/upload/cast')

    def __str__(self):
        return self.name


class Genre(models.Model):
    genre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.genre


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.DecimalField(default=0, decimal_places=1, max_digits=2)
    single_line_description = models.TextField()
    date_published = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    weekly_recommendation = models.BooleanField(default=False)
    cast = models.ManyToManyField(Cast, related_name='cast')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    poster = models.ImageField(default='default.jpg', upload_to='review/static/upload/poster')

    def __str__(self):
        return self.title


class Knowledge(models.Model):
    paragraph = models.TextField()

    def __str__(self):
        return self.paragraph
