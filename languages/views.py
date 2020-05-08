from django.shortcuts import render
from rest_framework import serializers
from .models import languages, paradigm, programmer
from .serializers import paradigmSerializer, languagesSerializer, programmerSerializer 
from rest_framework import viewsets, permissions

# Create your views here.
class paradigmViewSet(viewsets.ModelViewSet):
    queryset = paradigm.objects.all() 
    serializer_class = paradigmSerializer
    
class languagesViewSet(viewsets.ModelViewSet):
    queryset = languages.objects.all() 
    serializer_class = languagesSerializer

class programmerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all() 
    serializer_class = programmerSerializer     
