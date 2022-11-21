from datetime import time

from django.db import models

# Please add a Model class called Region
# To represent a sighting location
# A region has a name and a biome
class Region(models.Model):
    region = models.CharField(max_length=100)
    biome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.region}: {self.biome}"

# Create your models here.
class Sighting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(1))
    distance = models.IntegerField(default=1)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
