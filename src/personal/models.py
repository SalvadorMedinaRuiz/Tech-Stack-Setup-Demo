from django.db import models

# Create your models here. Where data structures are defined. Literally just make a class with a name variable. Make the list client side

class Persons(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name