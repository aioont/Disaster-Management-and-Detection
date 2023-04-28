from django.views.generic import TemplateView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.about, name='about'),
    
    path('disaster-detail/<int:disaster_report_id>/', views.DisasterDetail, name='disasterdetail'),
    path('volunteer_dashboard/', views.volunteer_dashboard, name='volunteer_dashboard'),  
    path('authority_dashboard/', views.authority_dashboard, name='authority_dashboard'),    
    path('authority_dashboard_edit/<int:disaster_report_id>/', views.authority_dashboard_edit, name='authority_dashboard_edit'),
    
    path('volunteer-register/', views.VolunteerRegisterPage, name='volunteerregister'),
    path('service-register/', views.ServiceRegisterPage, name='serviceregister'),
    path('shop-register/', views.ShopRegisterPage, name='shopregister'),
    path('hospital-register/', views.HospitalRegisterPage, name='hospitalregister'),
    path('near-volunteers/', views.NearVolunteer.as_view(), name='nearvolunteer'),
    path('near-service/', views.NearService.as_view(), name='serviceadmin'),
    path('login/',views.loginPage,name='loginPage'),
    path('forgot/',views.forgotPage,name='forgot'),
    path('signup/',views.signup,name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

