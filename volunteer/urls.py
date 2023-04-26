from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.about, name='about'),
    
    path('volunteer-register/', views.VolunteerRegisterPage, name='volunteerregister'),
    path('service-register/', views.ServiceRegisterPage, name='serviceregister'),
    path('shop-register/', views.ShopRegisterPage, name='shopregister'),
    path('hospital-register/', views.HospitalRegisterPage, name='hospitalregister'),
    path('near-volunteers/', views.NearVolunteer.as_view(), name='nearvolunteer'),
    path('near-service/', views.NearService.as_view(), name='serviceadmin'),
    path('login/',views.loginPage,name='loginPage'),
    path('forgot/',views.forgotPage,name='forgot'),
    path('signup/',views.signup,name='signup'),
]