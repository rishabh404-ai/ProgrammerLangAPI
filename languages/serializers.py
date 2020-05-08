from rest_framework import serializers
from .models import paradigm, languages, programmer

class paradigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = paradigm
        fields = ['id','url', 'name']

class languagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = languages
        fields = ['id','url', 'name', 'paradigm']

class programmerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = programmer
        fields = ['id','url', 'name', 'lang']                
