from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PatientModel)
admin.site.register(DoctorModel)