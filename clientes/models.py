from django.db import models

from contas.models import Empresa


class Cliente(models.Model):
    """Exemplo de área do negócio. Troque pelo que o PRD do projeto pede."""

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="clientes")
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ["nome"]
        constraints = [
            models.UniqueConstraint(
                fields=["empresa", "telefone"], name="telefone_unico_por_empresa"
            )
        ]

    def __str__(self):
        return self.nome
