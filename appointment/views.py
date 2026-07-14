from django.shortcuts import render
from .models import Doctor

def home(request):
    return render(request, 'appointment/home.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointment/doctors.html', {'doctors': doctors})