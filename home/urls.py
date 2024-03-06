
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", home),
    path("results/", views.home, name='results' ),
    # path("<int:id>/", views.detail , name='details'),
]
