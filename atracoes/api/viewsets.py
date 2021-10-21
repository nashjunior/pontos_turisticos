from rest_framework import viewsets
from atracoes.api.serializers import AtracoesSerializer
from atracoes.models import Atracao
class AtracoesViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer