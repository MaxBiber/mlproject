from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the math score page")

def about(request):
    return HttpResponse("This is the about us page")