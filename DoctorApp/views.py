from django.shortcuts import render
from .forms import *

def PatientSubmission(request):
    
    context = {
        'form' : PatientForm
    }
    
    return render(request,'submission.html',context=context)