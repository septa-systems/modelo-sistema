"""Fábricas de dados falsos para testes e para o seed (factory_boy + Faker em português)."""

import factory

from clientes.models import Cliente
from contas.models import Empresa, Usuario


class EmpresaFabrica(factory.django.DjangoModelFactory):
    class Meta:
        model = Empresa

    nome = factory.Faker("company", locale="pt_BR")


class UsuarioFabrica(factory.django.DjangoModelFactory):
    class Meta:
        model = Usuario

    username = factory.Sequence(lambda n: f"usuario{n}")
    empresa = factory.SubFactory(EmpresaFabrica)
    password = factory.django.Password("senha-de-teste-123")


class ClienteFabrica(factory.django.DjangoModelFactory):
    class Meta:
        model = Cliente

    empresa = factory.SubFactory(EmpresaFabrica)
    nome = factory.Faker("name", locale="pt_BR")
    telefone = factory.Sequence(lambda n: f"1199{n:07d}")
    email = factory.Faker("email", locale="pt_BR")
