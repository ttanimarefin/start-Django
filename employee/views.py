from django.shortcuts import render
from django.http import HttpResponse

def employee(request):
    return HttpResponse("This is Employee Page")

def profile(request):
    return render(request,'employee/profile.html')

# Create your views here.
