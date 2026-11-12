from django.contrib.auth.models import AbstractUser
from django.db import models


class Empresa(models.Model):
    """O negócio que usa o sistema. Cada empresa só vê os próprios dados."""

    nome = models.CharField(max_length=150)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "empresa"
        verbose_name_plural = "empresas"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Usuario(AbstractUser):
    """Quem entra no sistema. Pertence a uma empresa (o admin da Septa pode não ter)."""

    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.PROTECT,
        related_name="usuarios",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"
