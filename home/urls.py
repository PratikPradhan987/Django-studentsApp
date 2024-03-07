
from django.contrib import admin
from django.urls import path
from .view import *

urlpatterns = [
    path("", home),
    path("results/", results, name='results' ),
    # path("<int:id>/", views.detail , name='details'),
]
