from rest_framework.viewsets import ViewSet
from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico

class PontoTuristicoViewSet (ViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer