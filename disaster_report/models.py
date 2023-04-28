from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Disaster_report(models.Model):
    STATUS_CHOICES = (
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=200, unique=True)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    adress = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    # lat = models.FloatField(blank=True, default=True)
    # lng = models.FloatField(blank=True, default=True)
    location = models.PointField(null=True)
    images = models.ImageField(upload_to='disaster_images/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')

    def __str__(self):
        return self.name


# class Disaster_report(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     zipcode = models.CharField(max_length=200,blank=True, null=True)
#     city = models.CharField(max_length=200,blank=True, null=True)
#     country = models.CharField(max_length=200,blank=True, null=True)
#     adress = models.CharField(max_length=200,blank=True, null=True)
#     latitude = models.CharField(max_length=200,blank=True, null=True)
#     longitude = models.CharField(max_length=200,blank=True, null=True)
#     # lat = models.FloatField(blank=True, default=True)
#     # lng = models.FloatField(blank=True, default=True)
#     location = models.PointField(null=True)
#     images = models.ImageField(upload_to='disaster_images/', null=True, blank=True)


    def __str__(self):
        return self.name


# models.py
from django.db import models

# class Location(models.Model):
#     lat = models.FloatField()
#     lng = models.FloatField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"{self.user.username} - ({self.lat}, {self.lng})"
