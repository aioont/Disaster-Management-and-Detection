from django.db import models

# Create your models here.
class Disaster(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    impact = models.CharField(max_length=255)
    precautions = models.TextField()
    image = models.ImageField(upload_to='types_of_disaster_images/', blank=True, null=True)

    def __str__(self):
        return self.name
