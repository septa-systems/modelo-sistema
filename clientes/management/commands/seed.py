"""Cria dados FALSOS para o ambiente local e de teste (docs/AMBIENTES.md).

Uso: python manage.py seed
Nunca rode em produção: o comando se recusa se DEBUG=False, a não ser com --forcar-teste.
"""

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from clientes.tests.fabricas import ClienteFabrica, EmpresaFabrica, UsuarioFabrica
from contas.models import Empresa

SENHA = "senha-de-teste-123"


class Command(BaseCommand):
    help = "Cria empresas, usuários e clientes falsos para testar o sistema."

    def add_arguments(self, parser):
        parser.add_argument(
            "--forcar-teste",
            action="store_true",
            help="Permite rodar com DEBUG=False (só no ambiente de teste, nunca em produção).",
        )

    def handle(self, *args, **opcoes):
        if not settings.DEBUG and not opcoes["forcar_teste"]:
            raise CommandError(
                "DEBUG=False: parece produção. Use --forcar-teste só no ambiente de teste."
            )
        if Empresa.objects.exists():
            self.stdout.write("Já existem dados. Nada foi criado.")
            return

        for numero, nome in enumerate(["Padaria Exemplo", "Salão Exemplo"], start=1):
            empresa = EmpresaFabrica(nome=nome)
            UsuarioFabrica(username=f"empresa{numero}", empresa=empresa)
            ClienteFabrica.create_batch(15, empresa=empresa)

        self.stdout.write(self.style.SUCCESS("Dados falsos criados."))
        self.stdout.write(f"Entre com empresa1 ou empresa2, senha: {SENHA}")
