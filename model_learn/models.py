from django.db import models
from .conf import *

from django.core.validators import EmailValidator, MaxValueValidator
# Create your models here.


# ONE to MANY relationship

class Manufacturer(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length = 100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete = models.CASCADE)

    class Meta:
        ordering = ['-name']

    def __str__ (self):
        return self.name



# MANY to MANY realtionship
class Person(models.Model):
    name = models.CharField(max_length = 200)

    def __str__ (self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length = 200)
    # through fields to tell django that these fields are the endpoints of the relationship
    persons = models.ManyToManyField(Person, through='GroupRelation')

    def __str__ (self):
        return self.name

class GroupRelation(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    t = models.CharField(max_length = 100)


class Pizza(models.Model):
    name = models.CharField(
        max_length = 100, # need to migrate
        choices = PIZZA_CHOICE, # need to migrate
        blank = False, 
        null = False, # need to migrate
        help_text = "Something",
        # unique = True, # need to migrate
    )
    price = models.IntegerField(
        validators=[MaxValueValidator(500)]
    )



def upload_image(instance, name):
    return 'dp/' + instance.name + '/' + name

class buyer(models.Model):
    name = models.CharField(
        max_length = 100,
        validators = []
    )
    email = models.CharField(
        max_length = 200,
        validators = [EmailValidator]
    )
    isActive = models.NullBooleanField(
        null = True
    )

    attachment = models.FileField(upload_to='pictures/', null = True)

    dp = models.ImageField(upload_to=upload_image, null = True)

    timestamp = models.DateTimeField(auto_now=True)

