from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import *
from .models import *

from pyqrcode import create
import png
import base64

import os

from qrcode import *

def embed_QR(url_input, location_name):
    embedded_qr = create(url_input)
    embedded_qr.png(location_name, scale=7)


def PatientSubmissions(request):
    
    form = PatientForm()

    if request.method == 'POST':
        
        form = PatientForm(request.POST,request.FILES)
        
        if form.is_valid():    
            form.save()
        
        
        else:
            print(form.errors)
            return render(request,'submissions.html',context={'form':form,'errors':form.errors})
            # return redirect(reverse('submissions',kwargs={'form':form,'errors':form.errors}) + '#contact')
        

    patientsubs = PatientModel.objects.all()
    print("Patient subs: ", patientsubs)
    context = {
        'form' : form,
        'patientsubs':patientsubs
    }

    return render(request,'submissions.html',context=context)

def QRDownload(request,id):
    
    sub = PatientModel.objects.get(id=id)
    data = "Patient name: " + sub.name + "\n" + "Description: " + sub.description
    print("Data: ",data)
    
    img=make(data)
    img.save("static/QRs/" + sub.name + ".png")
    
    sub.qr = "Yes"
    sub.save()
    
    return redirect('/#services')

def QRDelete(request,id):

    sub = PatientModel.objects.get(id=id)
    filename = sub.name
    sub.delete()
    
    os.remove("static/QRs/"+filename+".png")
    
    return redirect('/#services')

