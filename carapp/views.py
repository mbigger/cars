from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
import random
# Create your views here.
def index(request):
    return render(request,"index.html")

def quiz(request):
    Qform = questionsform()
    gettingdata = questions.objects.all()
    getting = questions.objects.all().count()
    print(getting)
    quantity= 10
    tobe = []
    a= 1
    if(getting <10):
         quantity = getting

    while(a<= quantity):
        rand = int(random.random()*getting)
        selecting = questions.objects.all()[rand]
        
        
        if selecting in tobe:
                rand = int(random.random()*getting)
                selecting = questions.objects.all()[rand]
        else:
                tobe.append(selecting)
                a+=1

    print(tobe)
    return render( request,"quiz.html",{"form" : Qform,"data": gettingdata,"questions": tobe})
def login(request):
    return redirect("/admin")