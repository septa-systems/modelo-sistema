"""Views finas: recebem o pedido, conferem acesso e chamam o service."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from contas.permissoes import empresa_do_usuario

from . import services
from .forms import ClienteForm


@login_required
def lista(request):
    empresa = empresa_do_usuario(request)
    busca = request.GET.get("busca", "").strip()
    clientes = services.listar_clientes(empresa, busca=busca)
    contexto = {"clientes": clientes, "busca": busca, "form": ClienteForm()}

    # HTMX: na busca, devolve só a tabela, sem recarregar a página
    if request.htmx:
        return render(request, "clientes/_tabela.html", contexto)
    return render(request, "clientes/lista.html", contexto)


@login_required
@require_http_methods(["POST"])
def novo(request):
    empresa = empresa_do_usuario(request)
    form = ClienteForm(request.POST)
    if form.is_valid():
        try:
            services.cadastrar_cliente(empresa, **form.cleaned_data)
        except services.ClienteDuplicado:
            form.add_error("telefone", "Já existe um cliente com este telefone.")
        else:
            form = ClienteForm()

    contexto = {"form": form, "clientes": services.listar_clientes(empresa), "busca": ""}
    return render(request, "clientes/_painel.html", contexto)
