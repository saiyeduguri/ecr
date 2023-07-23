from django.shortcuts import render
from accounts.models import ROC,RAC,RMC,COP,REG

from django.http import HttpResponse

def index(request):
    a1=RAC.objects
    c1=a1.count() +100
    a2=RMC.objects
    c2=a2.count() +200
    a3=ROC.objects
    c3=a3.count() +200
    return render(request,"index.html",{'c1':c1,'c2':c2,'c3':c3})

