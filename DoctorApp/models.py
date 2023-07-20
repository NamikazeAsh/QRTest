from django.db import models
from django.core.validators import FileExtensionValidator

choices = (
    ('Orthopedic','Orthopedic'),
    ('Piles','Piles'),
    ('Fissures','Fissures'),
    ('Cataract','Cataract')
)

# Create your models here.
class PatientModel(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    pdfs = models.FileField(null=True,upload_to="pdfs",validators=[FileExtensionValidator(['pdf',""])])
    qr = models.CharField(max_length=100,default="No",null=True,blank=True)
    
    
class DoctorModel(models.Model):

    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100,choices=choices,default="-")
    clinic = models.CharField(max_length=100)
    qualification = models.CharField(max_length=500)
    experience = models.IntegerField()
    address = models.CharField(max_length=100)
    avail_timing = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} | {self.specialization}"
    
class DoctorUpload(models.Model):

    doctor = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    contact = models.CharField(max_length=100)
    pdfs = models.FileField(null=True,upload_to="pdfs",validators=[FileExtensionValidator(['pdf',""])])