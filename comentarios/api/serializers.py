from rest_framework import serializers
from comentarios.models import Comentario
class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('usuario', 'comentario', 'data', 'aprovado')