from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=30, decimal_places=20)
    longitude = models.DecimalField(max_digits=30, decimal_places=20)

    def __str__(self):
        return self.name