from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from sightings.models import Sighting

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
        {"sightings": Sighting.objects.all()})

def date(request):
    return HttpResponse("This page was served at " +str(datetime.now()))

# Please add: An about page that shows some text about yourself
def about(request):
    return HttpResponse("My name is kfly and I like to party.")

