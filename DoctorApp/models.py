from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class PatientModel(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    pdfs = models.FileField(null=True,upload_to="pdfs",validators=[FileExtensionValidator(['pdf',""])])