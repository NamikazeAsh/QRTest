from django import forms

from DoctorApp.models import *

class PatientForm(forms.ModelForm):

    name = forms.CharField(label="Name",widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    pdfs = forms.FileField(widget=forms.ClearableFileInput(attrs={'placeholder':'PDFs'}))
    
    class Meta:
        model = PatientModel
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['pdfs'].widget.attrs['class'] = 'form-control'
        


class DoctorUploadForm(forms.ModelForm):

    doctor = forms.ModelChoiceField(queryset=DoctorModel.objects.all())
    patient_name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    contact = forms.CharField(max_length=100)
    pdfs = forms.FileField(widget=forms.ClearableFileInput(attrs={'placeholder':'PDFs'}))