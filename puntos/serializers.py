
from rest_framework import serializers
from .models import Punto

class PuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punto
        fields = '__all__'
