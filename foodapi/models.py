from django.db import models


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=50, unique=True)
    genre = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

