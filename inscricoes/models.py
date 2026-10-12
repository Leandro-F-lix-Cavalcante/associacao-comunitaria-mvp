from django.db import models
from participantes.models import Participante
from atividades.models import Atividade


class Inscricao(models.Model):
    STATUS_CHOICES = [
        ("ativa", "Ativa"),
        ("cancelada", "Cancelada"),
    ]

    participante = models.ForeignKey(
        Participante,
        on_delete=models.PROTECT,
        related_name="inscricoes"
    )

    atividade = models.ForeignKey(
        Atividade,
        on_delete=models.PROTECT,
        related_name="inscricoes"
    )

    data_inscricao = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ativa"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["participante", "atividade"],
                condition=models.Q(status="ativa"),
                name="inscricao_ativa_unica"
            )
        ]

    def __str__(self):
        return f"{self.participante} - {self.atividade}"