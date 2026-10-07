from django.db import models


class Participante(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome