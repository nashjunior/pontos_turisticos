from rest_framework import viewsets
from comentarios.api.serializers import ComentariosSerializer
from comentarios.models import Comentario
class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer