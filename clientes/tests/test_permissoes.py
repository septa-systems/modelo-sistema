"""Permissões: obrigatório em todo sistema (docs/SEGURANCA.md).

Quem não entrou é mandado para o login, e a empresa A nunca vê dados da empresa B.
"""

import pytest
from django.urls import reverse

from .fabricas import ClienteFabrica, EmpresaFabrica, UsuarioFabrica

pytestmark = pytest.mark.django_db


def test_sem_login_vai_para_a_tela_de_entrar(client):
    resposta = client.get(reverse("clientes:lista"))

    assert resposta.status_code == 302
    assert reverse("login") in resposta.url


def test_sem_login_nao_cadastra(client):
    resposta = client.post(reverse("clientes:novo"), {"nome": "X", "telefone": "11988887777"})

    assert resposta.status_code == 302


def test_empresa_a_nao_ve_clientes_da_empresa_b(client):
    usuario_a = UsuarioFabrica()
    ClienteFabrica(empresa=usuario_a.empresa, nome="Cliente da A")
    ClienteFabrica(empresa=EmpresaFabrica(), nome="Cliente da B")
    client.force_login(usuario_a)

    resposta = client.get(reverse("clientes:lista"))

    assert "Cliente da A" in resposta.text
    assert "Cliente da B" not in resposta.text


def test_cliente_cadastrado_fica_na_empresa_de_quem_cadastrou(client):
    usuario = UsuarioFabrica()
    client.force_login(usuario)

    client.post(reverse("clientes:novo"), {"nome": "Novo", "telefone": "(11) 97777-6666"})

    assert usuario.empresa.clientes.filter(nome="Novo").exists()


def test_usuario_sem_empresa_e_bloqueado(client):
    client.force_login(UsuarioFabrica(empresa=None))

    resposta = client.get(reverse("clientes:lista"))

    assert resposta.status_code == 403
