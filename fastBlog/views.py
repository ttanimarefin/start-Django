from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("This is about Page")

def contact(request):
    return HttpResponse("This is contact Page")