from django.contrib import admin
from .models import Doctor, Patient, Appointment

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)

admin.site.site_header = "Clinic Appointment System"
admin.site.site_title = "Clinic Admin"
admin.site.index_title = "Welcome to Clinic Appointment Dashboard"