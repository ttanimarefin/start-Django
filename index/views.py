from django.shortcuts import render
from .models import about
# Create your views here.
from django.http import HttpResponse

def home(request):
    aboutdata=about.objects.all()
    context={
        'about':aboutdata
    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contact.html')