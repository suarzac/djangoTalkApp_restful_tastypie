from django.db import models

# Create your models here.

class Talk(models.Model):
    name = models.CharField(max_length=200)
    speaker = models.CharField(max_length=200)
    venue = models.CharField(default= 'Zoom', max_length=200)
    duration = models.DecimalField(decimal_places= 2, max_digits= 8, default=0)

    def __str__(self):
        return self.name
