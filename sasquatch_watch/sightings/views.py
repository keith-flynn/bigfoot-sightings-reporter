from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Sighting, Region

# Create your views here.
def detail(request, id):
    sighting = get_object_or_404(Sighting, pk=id)
    return render(request, "sightings/detail.html", {"sighting": sighting})

# Please add a new page that shows a list of all region objects
def regions_list(request):
    return render(request, "sightings/regions_list.html", 
    {"regions": Region.objects.all()})

SightingForm = modelform_factory(Sighting, exclude=[])

def new(request):
    if request.method == "POST":
        # form has been submitted, process data
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = SightingForm()
        return render(request, "sightings/new.html", {"form": form})