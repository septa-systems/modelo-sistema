# Modelo de sistema da Septa Systems

Ponto de partida de todo sistema da Septa: **Django + PostgreSQL + HTMX + Tailwind**, tudo no Docker, já com login seguro, acesso separado por empresa, testes e as regras do time.

## Começar um sistema novo

1. **Use this template → Create a new repository** (dono: `septa-systems`).
   Nome: `sistema-<cliente>`. Projeto de cliente é **privado**.
2. No repositório novo:
   - Settings → General: só "Squash merge" e "Automatically delete head branches".
   - Settings → Code security: ligue Dependabot.
   - Repositório público: Settings → Rules, regra da `main` igual à do manual (PR + aprovação do Tech lead + checagens "Padrão do time" e "Sistema"). Privado no plano grátis: vale a Regra nº 1 do `CLAUDE.md`.
3. Antes de programar: `docs/projeto/` (entrevista, PRD e arquitetura). Ver `docs/projeto/README.md`.
4. Troque o app de exemplo `clientes` pelo que o PRD pede, no mesmo jeito: service + permissão + testes.

## Rodar no PC

Precisa só do **Docker**.

```bash
cp .env.example .env
docker compose up                 # abre em http://localhost:8000
```

Em outro terminal:

```bash
docker compose exec web python manage.py seed                 # dados falsos
docker compose exec web python manage.py createsuperuser      # seu usuário do admin
docker compose exec web python manage.py criar_2fa <usuario>  # 2FA do admin
```

Entre com `empresa1` ou `empresa2`, senha `senha-de-teste-123` (só dados falsos).
Admin: `http://localhost:8000/painel-interno/` (pede o código do app autenticador).

Porta 8000 ocupada? `PORTA=8001 docker compose up`.

### Antes de abrir o PR (o mesmo que a checagem do GitHub roda)

```bash
docker compose exec web sh -c "ruff format . && ruff check . && python manage.py makemigrations --check --dry-run && pytest"
```

Opcional: `pip install pre-commit && pre-commit install` formata sozinho a cada commit.

## O que já vem pronto

| | |
|---|---|
| **Login** | limite de 5 tentativas (django-axes), senha mínima de 8 |
| **Admin** | fora de `/admin/` e só com 2FA (django-otp) |
| **Acesso por empresa** | `contas/permissoes.py`: empresa A nunca vê dados da empresa B, com teste |
| **Produção segura** | HTTPS, cookies seguros, HSTS; `check --deploy` sem avisos |
| **12-Factor** | tudo que muda por ambiente vem do `.env` |
| **Testes** | pytest + factory_boy: regras, permissões, login e telas |
| **Telas** | HTMX (busca e cadastro sem recarregar) + Tailwind sem Node |
| **Deploy** | `Dockerfile` pronto (gunicorn, whitenoise, migrations no início); rota `/saude/` |

## Estrutura

```
config/                 # settings (lê o .env), urls
contas/                 # Empresa, Usuario, permissões, comando criar_2fa
clientes/               # EXEMPLO de área do negócio
├── models.py           # dados
├── services.py         # regras de negócio
├── views.py            # fina: confere acesso e chama o service
├── forms.py
├── management/commands/seed.py
└── tests/              # fabricas, services, permissões, views
templates/              # base, login, telas (parciais HTMX começam com _)
assets/css/fonte.css    # cores (Tailwind)
static/js/htmx.min.js
docs/projeto/           # entrevista, PRD, arquitetura, ADRs
```

## Regras do time

Tudo em [septa-handbook](https://github.com/septa-systems/septa-handbook). O Claude segue o `CLAUDE.md` deste repositório.
