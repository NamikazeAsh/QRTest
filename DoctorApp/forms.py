from django import forms

from DoctorApp.models import *

class PatientForm(forms.ModelForm):

    name = forms.CharField(label="Name",widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    pdfs = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'placeholder':'PDFs'}))
    
    class Meta:
        model = PatientModel
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['pdfs'].widget.attrs['class'] = 'form-control'
        
    