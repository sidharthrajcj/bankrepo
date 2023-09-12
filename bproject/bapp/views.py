# views.py
from django.shortcuts import render
from .models import District

def district_dropdown(request):
    districts = District.objects.all()
    return render(request, 'base.html', {'districts': districts})

def home(request):
    return render(request,'home.html')

