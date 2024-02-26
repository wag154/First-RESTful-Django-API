from django.db import models

class Drink (models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)

    # change display name for the object on admin panel 
    def __str__(self):
        return self.name + '' + self.description