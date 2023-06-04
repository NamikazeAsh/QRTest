from django import forms

from DoctorApp.models import *

class PatientForm(forms.ModelForm):

    name = forms.CharField()
    description = forms.CharField()
    pdfs = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    
    class Meta:
        model = PatientModel
        fields = "__all__"
    