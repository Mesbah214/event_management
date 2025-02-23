from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    category = models.ForeignKey(
        "Category", on_delete=models.DO_NOTHING, null=False, default=1)

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    event = models.ManyToManyField(Event)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
