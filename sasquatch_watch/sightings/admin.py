from django.contrib import admin

from .models import Sighting, Region

# Register your models here.
admin.site.register(Sighting)
admin.site.register(Region)