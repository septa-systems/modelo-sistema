"""Regras de acesso usadas por todas as views (docs/SEGURANCA.md).

Toda view que mostra dados de empresa usa `empresa_do_usuario`: assim é impossível
esquecer o filtro e mostrar dados de uma empresa para outra.
"""

from django.core.exceptions import PermissionDenied

from .models import Empresa


def empresa_do_usuario(request) -> Empresa:
    """Devolve a empresa de quem está logado, ou bloqueia (403) se não tiver."""
    empresa = getattr(request.user, "empresa", None)
    if empresa is None:
        raise PermissionDenied("Usuário sem empresa.")
    return empresa
