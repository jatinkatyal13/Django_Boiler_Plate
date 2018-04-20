from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length = 100)
    website = models.URLField()

    def __str__ (self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length = 200)
    score = models.IntegerField(default = 1)

    def __str__ (self):
        return self.name

class Entry(models.Model):
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)
    author = models.ManyToManyField(Author)