from django.shortcuts import render
from .forms import *

def PatientSubmission(request):

    form = PatientForm()

    if request.method == 'POST':
        
        form = PatientForm(request.POST,request.FILES)
        
        if form.is_valid():    
            form.save()
            return render(request,'submission.html',context={'form':form})
        
        
        else:
            print(form.errors)
            return render(request,'submission.html',context={'form':form,'errors':form.errors})
        

    context = {
        'form' : form
    }

    return render(request,'submission.html',context=context)

def PatientSubmissions(request):
    return render(request,'submissions.html')
