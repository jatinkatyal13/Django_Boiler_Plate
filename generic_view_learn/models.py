from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 100)
    score = models.IntegerField(default = 1)

    def __str__ (self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.TextField(blank = True, null = True)
    slug = models.SlugField(blank = True, null = True)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    def save(self, *args, **kwargs):
        if self.slug == "" or not self.slug:
            self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)
    
    def __str__ (self):
        return self.name
