from django.http import HttpResponse

def home(request):
    return HttpResponse("This is Home Page")

def about(request):
    return HttpResponse("This is about Page")

def contact(request):
    return HttpResponse("This is contact Page")