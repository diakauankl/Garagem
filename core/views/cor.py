from rest_framework.viewsets import ModelViewSet

from core.models import cor
from core.serializers import CorSerializer


class CorViewSet(ModelViewSet):
    queryset = cor.Cor.objects.all()
    serializer_class = CorSerializer
