import rest_framework.serializers as serializers

from core.models import PontoTuristico

class PontoTuristicoSerializer (serializers.ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao')