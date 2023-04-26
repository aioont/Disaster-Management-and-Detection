from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Disaster

def disaster_detail(request, disaster_id):
    disaster = get_object_or_404(Disaster, pk=disaster_id)
    return render(request, 'disaster_details.html', {'disaster': disaster})

def TypeOfDisaster(request):
    disasters = Disaster.objects.all()
    return render(request, 'TypeOfDisaster.html', {'disasters': disasters})
