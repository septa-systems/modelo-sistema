"""Regras de negócio de clientes (docs/ARQUITETURA.md: a regra mora aqui, a view só chama).

Toda função recebe a empresa: nada aqui consegue ver dados de outra empresa.
"""

import re

from django.db.models import QuerySet

from contas.models import Empresa

from .models import Cliente


class ClienteDuplicado(Exception):
    """Já existe cliente com este telefone nesta empresa."""


def normalizar_telefone(telefone: str) -> str:
    """Deixa só os números: '(11) 98888-7777' vira '11988887777'."""
    return re.sub(r"\D", "", telefone)


def listar_clientes(empresa: Empresa, busca: str = "") -> QuerySet[Cliente]:
    clientes = Cliente.objects.filter(empresa=empresa)
    if busca:
        clientes = clientes.filter(nome__icontains=busca)
    return clientes


def cadastrar_cliente(empresa: Empresa, nome: str, telefone: str, email: str = "") -> Cliente:
    telefone = normalizar_telefone(telefone)
    if Cliente.objects.filter(empresa=empresa, telefone=telefone).exists():
        raise ClienteDuplicado(telefone)
    return Cliente.objects.create(
        empresa=empresa, nome=nome.strip(), telefone=telefone, email=email.strip().lower()
    )
