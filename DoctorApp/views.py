from django.shortcuts import render
from .forms import *

def PatientSubmissions(request):
    
    form = PatientForm()

    if request.method == 'POST':
        
        form = PatientForm(request.POST,request.FILES)
        
        if form.is_valid():    
            form.save()
            return render(request,'submissions.html',context={'form':form})
        
        
        else:
            print(form.errors)
            return render(request,'submissions.html',context={'form':form,'errors':form.errors})
        

    context = {
        'form' : form
    }

    return render(request,'submissions.html',context=context)
