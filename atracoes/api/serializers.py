from rest_framework import serializers
from atracoes.models import Atracao

class AtracoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('nome', 'descricao', 'horario_funcionamento', 'idade_minima')