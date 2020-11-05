from django.db import models


# Create your models here.
class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    surname = models.TextField()
    year = models.IntegerField()


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    year = models.IntegerField()
    annotation = models.TextField()
