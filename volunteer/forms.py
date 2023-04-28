from django.contrib.auth import get_user_model
from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from disaster_report.models import Disaster_report

class DisasterFormEdit(forms.ModelForm):
    class Meta:
        model = Disaster_report
        fields = '__all__'
        exclude = ['location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'zipcode': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'city': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'country': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'address': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'latitude': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'longitude': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'description': forms.Textarea(attrs={'class': 'textarea textarea-bordered textarea-primary w-full max-w-xs'}),
            'status': forms.Select(choices=Disaster_report.STATUS_CHOICES)
        }




class VolunteerForm(ModelForm):

    class Meta:
        model = Volunteer
        exclude = ['user','volunteer_email']  # exclude user field from the form
        widgets = {     
            'volunteer_mobile': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'volunteer_address': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'volunteer_skills': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
        }




class ServiceForm(ModelForm):

    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'service_name': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'service_email': forms.EmailInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'service_mobile': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'service_address': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'service_type': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
        }
        


class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
        widgets = {
            'service_name': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'service_email': forms.EmailInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'service_mobile': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'service_address': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'service_type': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
        }     

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        widgets = {
            'shop_name': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'shop_detail': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'shop_type': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
            'shop_contact': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
        }   



class UserAdminCreationForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('authority', 'Authority'),
        ('volunteer', 'Volunteer'),
        ('user', 'User')
    )

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'mobile', 'email', 'user_type', 'password1', 'password2']




