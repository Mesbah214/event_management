from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def all_events(request):
    return render(request, 'events.html')

def dashboard(request):
    return render(request, 'home.html')

def categories(request):
    return render(request, 'categories.html')

def participants(request):
    return render(request, 'participants.html')

def new_event(request):
    return render(request, 'new_event.html')

def details_event(request):
    return render(request, 'details_event.html')