from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)

    def __str__(self):
        return self.name 
