from django.http import HttpResponse

def employee(request):
    return HttpResponse("This is Employee Page")

def profile(request):
    return HttpResponse("This is Employee Profile Page")

# Create your views here.
