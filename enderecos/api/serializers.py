from rest_framework import serializers
from enderecos.models import Endereco
class EnderecosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('linha1', 'linha2', 'cidade', 'estado', 'pais', 'latitude', 'longitude')