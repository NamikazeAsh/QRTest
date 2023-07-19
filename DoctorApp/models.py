from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class PatientModel(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    pdfs = models.FileField(null=True,upload_to="pdfs",validators=[FileExtensionValidator(['pdf',""])])
    qr = models.CharField(max_length=100,default="No",null=True,blank=True)
    
    
class DoctorModel(models.Model):

    name = models.CharField(max_length=100)
    clinic = models.CharField(max_length=100)
    qualification = models.CharField(max_length=500)
    experience = models.IntegerField()
    address = models.CharField(max_length=100)
    avail_timing = models.CharField(max_length=100)
    city = models.CharField(max_length=100)