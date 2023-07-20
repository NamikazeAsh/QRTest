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

    doctor = forms.ModelChoiceField(queryset=DoctorModel.objects.all(),widget=forms.TextInput(attrs={'placeholder':'Doctor Name'}))
    patient_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Patient Name'}))
    description = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'placeholder':'Disease Description'}))
    contact = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Email or Phone Number'}))
    pdfs = forms.FileField(widget=forms.ClearableFileInput(attrs={'placeholder':'PDFs'}))
    
    class Meta:
        model = DoctorUpload
        fields = ('doctor','patient_name','description','contact','pdfs')
        
    def __init__(self, *args, **kwargs):
        super(DoctorUploadForm, self).__init__(*args, **kwargs)
        self.fields['patient_name'].widget.attrs['class'] = 'street'
        self.fields['description'].widget.attrs['class'] = 'street'
        self.fields['contact'].widget.attrs['class'] = 'street'
        self.fields['pdfs'].widget.attrs['class'] = 'street'
        
        self.fields['doctor'].required  = False