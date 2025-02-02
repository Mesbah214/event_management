from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is home")

def show_events(request):
    return HttpResponse("Show all events")