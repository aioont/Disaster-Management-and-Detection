from django.urls import path
from . import views

urlpatterns = [
    path('type-of-disasters/', views.TypeOfDisaster, name='type-of-disasters'),
    path('type-of-disasters/<int:disaster_id>/', views.disaster_detail, name='disaster_detail'),
]