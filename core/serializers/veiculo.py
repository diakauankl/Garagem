from rest_framework import serializers

from core.models import veiculo


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = veiculo.Veiculo
        fields = '__all__'
