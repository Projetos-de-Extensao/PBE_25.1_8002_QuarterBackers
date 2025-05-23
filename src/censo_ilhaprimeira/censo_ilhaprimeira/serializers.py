from rest_framework import serializers
from .models import Morador, Domicilio

class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'

class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields = '__all__'