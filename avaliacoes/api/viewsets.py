from rest_framework import viewsets
from avaliacoes.api.serializers import AvaliacoesSerializer
from avaliacoes.models import Avaliacao

class AvaliacoesViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacoesSerializer