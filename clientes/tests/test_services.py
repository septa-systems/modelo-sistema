"""Regras de negócio: o teste mais importante (docs/PADROES.md)."""

import pytest

from clientes.services import ClienteDuplicado, cadastrar_cliente, listar_clientes

from .fabricas import ClienteFabrica, EmpresaFabrica

pytestmark = pytest.mark.django_db


def test_cadastra_cliente_com_telefone_so_numeros():
    empresa = EmpresaFabrica()

    cliente = cadastrar_cliente(empresa, nome=" Ana Souza ", telefone="(11) 98888-7777")

    assert cliente.nome == "Ana Souza"
    assert cliente.telefone == "11988887777"


def test_nao_cadastra_telefone_repetido_na_mesma_empresa():
    empresa = EmpresaFabrica()
    cadastrar_cliente(empresa, nome="Ana", telefone="11988887777")

    with pytest.raises(ClienteDuplicado):
        cadastrar_cliente(empresa, nome="Outra Ana", telefone="(11) 98888-7777")


def test_mesmo_telefone_pode_existir_em_empresas_diferentes():
    cadastrar_cliente(EmpresaFabrica(), nome="Ana", telefone="11988887777")

    cliente = cadastrar_cliente(EmpresaFabrica(), nome="Ana", telefone="11988887777")

    assert cliente.pk is not None


def test_lista_so_clientes_da_propria_empresa():
    empresa_a, empresa_b = EmpresaFabrica(), EmpresaFabrica()
    do_a = ClienteFabrica(empresa=empresa_a)
    ClienteFabrica(empresa=empresa_b)

    assert list(listar_clientes(empresa_a)) == [do_a]


def test_busca_por_nome_sem_diferenciar_maiusculas():
    empresa = EmpresaFabrica()
    ana = ClienteFabrica(empresa=empresa, nome="Ana Souza")
    ClienteFabrica(empresa=empresa, nome="Bruno Lima")

    assert list(listar_clientes(empresa, busca="ana")) == [ana]
