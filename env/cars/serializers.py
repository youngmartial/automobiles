from rest_framework import serializers
from .models import cars

class carserializer(serializers.ModelSerializer):
    class Meta:
        Model = cars
        fields = ['id', 'name', 'description']
