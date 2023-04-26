from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserAdminCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import *
from .models import *
from django.views import generic

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from disaster_report.models import Disaster_report



longitude = Disaster_report().longitude
latitude = Disaster_report().latitude

user_location = Point(longitude, latitude, srid=4326)


class NearVolunteer(generic.ListView):
    model = CustomUser
    context_object_name = 'shops'
    queryset = CustomUser.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:3]
    template_name = 'nearvolunteers.html'

longitude = Disaster_report().longitude
latitude = Disaster_report().latitude
service_location = Point(longitude, latitude, srid=4326)

class NearService(generic.ListView):
    model = ServiceAdmin
    context_object_name = 'service'
    queryset = ServiceAdmin.objects.annotate(distance=Distance('serviceadmin_locations',
    service_location)
    ).order_by('distance')[0:3]
    template_name = 'nearservice.html'

# Create your views here.


# @login_required(login_url='login')


def homePage(request):
    latest_disasters = Disaster_report.objects.order_by('-id')[:5]
    context = {'latest_disasters': latest_disasters}
    return render(request, 'index.html', context)


def VolunteerRegisterPage(request):

    form = VolunteerForm()
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()


            # messages.success(request, 'Account Created for ' + user + ' Please login')
            return redirect('home')
    return render(request, 'volunteerregister.html', {'form': form})

def ServiceRegisterPage(request):

    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()

            # messages.success(request, 'Account Created for ' + user + ' Please login')
            return redirect('home')
    return render(request, 'serviceregister.html', {'form': form})

@login_required
def ShopRegisterPage(request):
    form = ShopForm()
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted')
            return redirect('home')
    return render(request, 'shopregister.html', {'form': form})

@login_required
def HospitalRegisterPage(request):

    form = HospitalForm()
    if request.method == 'POST':
        form = Hospital(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted')
            return redirect('home')
    return render(request, 'hospitalregister.html', {'form': form})





def loginPage(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, 'Password or Username is incorrect')
            

    return render(request, 'login.html')



def signup(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_type = form.cleaned_data.get('user_type')
            user.user_type = user_type
            user.save()

            username = form.cleaned_data.get('first_name')

            messages.success(request, 'Account Created for ' + str(user) + ' Please login')
            return redirect('loginPage')
    return render(request, 'signup.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def forgotPage(request):
    return render(request, 'forgot.html')
