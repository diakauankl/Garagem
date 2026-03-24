from rest_framework.viewsets import ModelViewSet

from core.models import modelo
from core.serializers import modeloSerializer


class ModeloViewSet(ModelViewSet):
    queryset = modelo.Modelo.objects.all()
    serializer_class = modeloSerializer.ModeloSerializer
