"""Cria o código de verificação em 2 etapas (2FA) de um usuário para entrar no admin.

Uso: python manage.py criar_2fa <usuario>
Depois, leia o QR code (ou digite a chave) no Google Authenticator, Microsoft
Authenticator ou Bitwarden. No login do admin, use o código de 6 números do app.
"""

import io

import qrcode
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django_otp.plugins.otp_totp.models import TOTPDevice


class Command(BaseCommand):
    help = "Cria o 2FA (app autenticador) de um usuário para entrar no admin."

    def add_arguments(self, parser):
        parser.add_argument("usuario")

    def handle(self, *args, **opcoes):
        Usuario = get_user_model()
        try:
            usuario = Usuario.objects.get(username=opcoes["usuario"])
        except Usuario.DoesNotExist as erro:
            raise CommandError("Usuário não encontrado.") from erro

        TOTPDevice.objects.filter(user=usuario).delete()
        aparelho = TOTPDevice.objects.create(user=usuario, name="app autenticador", confirmed=True)

        qr = qrcode.QRCode(border=1)
        qr.add_data(aparelho.config_url)
        saida = io.StringIO()
        qr.print_ascii(out=saida, invert=True)

        self.stdout.write(saida.getvalue())
        self.stdout.write("Leia o QR code acima no app autenticador.")
        self.stdout.write(f"Ou adicione manualmente este link no app: {aparelho.config_url}")
        self.stdout.write(self.style.WARNING("Não salve este link em lugar nenhum além do app."))
