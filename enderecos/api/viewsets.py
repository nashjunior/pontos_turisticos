from rest_framework import viewsets
from enderecos.api.serializers import EnderecosSerializer
from enderecos.models import Endereco

class EnderecosViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerializer