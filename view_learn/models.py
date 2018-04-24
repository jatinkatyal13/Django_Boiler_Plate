from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.name