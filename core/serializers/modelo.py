from rest_framework import serializers

from core.models import modelo


class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = modelo.Modelo
        fields = '__all__'
