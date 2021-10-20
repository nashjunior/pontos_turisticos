from django.db import models
from atracoes.models import Atracao as Atracoes
from comentarios.models import Comentario as Comentarios
from avaliacoes.models import Avaliacao as Avaliacoes
from enderecos.models import Endereco

# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    status = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracoes)
    comentarios = models.ManyToManyField(Comentarios)
    avaliacoes = models.ManyToManyField(Avaliacoes)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nome