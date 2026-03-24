from rest_framework import serializers

from core.models import acessorio


class AcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = acessorio.Acessorio
        fields = '__all__'
