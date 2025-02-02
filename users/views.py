from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_users(request):
    return HttpResponse("show all users")