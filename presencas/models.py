from django.db import models
from inscricoes.models import Inscricao


class Presenca(models.Model):
    inscricao = models.OneToOneField(
        Inscricao,
        on_delete=models.CASCADE,
        related_name="presenca"
    )
    presente = models.BooleanField(default=False)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.inscricao} - {'Presente' if self.presente else 'Ausente'}"