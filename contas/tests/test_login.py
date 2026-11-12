"""Segurança do login (docs/SEGURANCA.md): limite de tentativas e admin fora de /admin/."""

import pytest
from django.conf import settings
from django.urls import reverse

from clientes.tests.fabricas import UsuarioFabrica

pytestmark = pytest.mark.django_db


def test_login_bloqueia_depois_de_5_senhas_erradas(client):
    usuario = UsuarioFabrica()
    for _ in range(settings.AXES_FAILURE_LIMIT):
        client.post(reverse("login"), {"username": usuario.username, "password": "errada"})

    resposta = client.post(
        reverse("login"), {"username": usuario.username, "password": "senha-de-teste-123"}
    )

    assert resposta.status_code == 429


def test_login_com_senha_certa_entra(client):
    usuario = UsuarioFabrica()

    resposta = client.post(
        reverse("login"), {"username": usuario.username, "password": "senha-de-teste-123"}
    )

    assert resposta.status_code == 302


def test_admin_nao_fica_em_barra_admin(client):
    assert client.get("/admin/").status_code == 404
