from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

mode_of_transport = [
  ("Driving","driving"),
  ("Bicycling","bicycling"),
  ("Walking","walking"),
  ("Transit","transit"),
]
# class DisasterForm(ModelForm):

#     class Meta:
#         model = Disaster_report
#         fields = ['name', 'zipcode', 'city', 'country', 'adress', 'latitude', 'longitude',  'images']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
#             'zipcode': forms.EmailInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
#             'city': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
#             'country': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
#             'adress': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
#             'latitude': 

#         }   


class DisasterForm(forms.ModelForm):
    class Meta:
        model = Disaster_report
        fields = ['name', 'zipcode', 'city', 'country', 'adress', 'latitude', 'longitude', 'location', 'images']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'zipcode': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'city': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'country': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'adress': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'latitude': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'longitude': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
          
            'images': forms.ClearableFileInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
        }


