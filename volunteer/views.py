from django.shortcuts import render, redirect, get_object_or_404
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
from django.contrib.auth.decorators import user_passes_test


from django.shortcuts import get_object_or_404, redirect, render
from .forms import DisasterFormEdit
from disaster_report.models import Disaster_report

longitude = Disaster_report().longitude
latitude = Disaster_report().latitude

user_location = Point(longitude, latitude, srid=4326)

#Near volunteers
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

#Near services
class NearService(generic.ListView):
    model = ServiceAdmin
    context_object_name = 'service'
    queryset = ServiceAdmin.objects.annotate(distance=Distance('serviceadmin_locations',
    service_location)
    ).order_by('distance')[0:3]
    template_name = 'nearservice.html'




@login_required
def DisasterDetail(request, disaster_report_id):
    disaster_reports = get_object_or_404(Disaster_report, id=disaster_report_id)
    print(disaster_reports) 

    context ={'disaster_reports': disaster_reports}
    return render(request, 'disaster_detail.html', context)






@login_required
def authority_dashboard_edit(request, disaster_report_id):
    disaster_reports = get_object_or_404(Disaster_report, id=disaster_report_id)
    print(disaster_reports)
    if request.method == 'POST':
        form = DisasterFormEdit(request.POST, instance=disaster_reports)
        if form.is_valid():
            form.save()
            return redirect('authority_dashboard')
    else:
        form = DisasterFormEdit(instance=disaster_reports)

    context = {'form': form, 'disaster_reports': disaster_reports}
    return render(request, 'authority_dashboard_edit.html', context)


def authority_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == 'authority':
        disaster_reports = Disaster_report.objects.all()
        context = {'disaster_reports': disaster_reports}
    else:
        context = {}

    return render(request, 'authority_dashboard.html', context)


def volunteer_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == 'volunteer':
        disaster_reports = Disaster_report.objects.all()
        context = {'disaster_reports': disaster_reports}
    else:
        context = {}

    return render(request, 'volunteer_dashboard.html', context)



# @login_required(login_url='login')


def homePage(request):
    latest_disasters = Disaster_report.objects.order_by('-id')[:5]
    context = {'latest_disasters': latest_disasters}
    return render(request, 'index.html', context)






@login_required
def VolunteerRegisterPage(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.user = request.user
            volunteer.save()
            
            # Update user_type for the current user
            user = request.user
            user.user_type = 'volunteer'
            user.save()
            
            return redirect('home')
    else:
        form = VolunteerForm()
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
