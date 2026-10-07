from django.db import models


class Atividade(models.Model):
    STATUS_CHOICES = [
        ("ativa", "Ativa"),
        ("cancelada", "Cancelada"),
        ("encerrada", "Encerrada"),
    ]

    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateField()
    horario = models.TimeField()
    vagas = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ativa"
    )

    class Meta:
        ordering = ["data", "horario"]

    def __str__(self):
        return self.nome