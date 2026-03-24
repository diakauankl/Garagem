from rest_framework import serializers

from core.models import cor


class CorSerializer(serializers.ModelSerializer):
    class Meta:
        model = cor.Cor
        fields = '__all__'
