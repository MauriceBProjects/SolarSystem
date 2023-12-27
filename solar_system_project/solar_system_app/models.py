from django.db import models

# Create model for planets

class Planet(models.Model):
    name = models.CharField(max_length=100)
    order_from_sun = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField()
