"""Telas: poucos testes, só os caminhos principais (pirâmide de testes)."""

import pytest
from django.urls import reverse

from .fabricas import ClienteFabrica, UsuarioFabrica

pytestmark = pytest.mark.django_db


@pytest.fixture
def logado(client):
    usuario = UsuarioFabrica()
    client.force_login(usuario)
    return client, usuario


def test_busca_com_htmx_devolve_so_a_tabela(logado):
    client, usuario = logado
    ClienteFabrica(empresa=usuario.empresa, nome="Ana Souza")

    resposta = client.get(reverse("clientes:lista"), {"busca": "ana"}, HTTP_HX_REQUEST="true")

    assert "Ana Souza" in resposta.text
    assert "<html" not in resposta.text


def test_telefone_repetido_mostra_erro_no_formulario(logado):
    client, usuario = logado
    ClienteFabrica(empresa=usuario.empresa, telefone="11988887777")

    resposta = client.post(reverse("clientes:novo"), {"nome": "Ana", "telefone": "11988887777"})

    assert "Já existe um cliente com este telefone." in resposta.text


def test_saude_responde_ok(client):
    assert client.get(reverse("saude")).text == "ok"
