from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('addPerson/',AddPerson.as_view(), name = 'addPerson'),
    #path('addFamily/',views.AddFamily.as_view()),
    # path('deletePerson/',views.DeletePerson.as_view()),
]