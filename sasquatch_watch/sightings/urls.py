from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('regions', views.regions_list, name="regions"),
    path('new', views.new, name="new")
]
