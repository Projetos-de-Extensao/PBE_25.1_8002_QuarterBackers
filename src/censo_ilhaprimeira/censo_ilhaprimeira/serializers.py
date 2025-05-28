from rest_framework import serializers
from .models import Morador, Domicilio, Falecido

class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'

class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields = '__all__'

class FalecidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Falecido
        fields = '__all__'