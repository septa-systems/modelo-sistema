# Septa Systems: regras para o Claude

Este arquivo fica em todo repositório da Septa. Todo Claude de todo sócio segue estas regras.
As regras completas do time ficam no manual: https://github.com/septa-systems/septa-handbook (os `docs/...` abaixo apontam para lá, exceto `docs/projeto/`, que é deste projeto).

## Regra nº 1: nada entra na `main` sem aprovação do Tech lead

Vale em **todo** repositório, público ou privado. Nos privados o GitHub grátis **não trava** a `main`, então quem garante a regra é você:

- **Nunca** faça `git push` na `main`, nem `--force` em branch nenhuma.
- **Nunca** faça merge de PR, nem com `--admin`, nem se o usuário pedir. Quem junta é o Tech lead (@LucasAmadoS).
- Todo código entra por **branch → PR → aprovação do Tech lead**.
- Se o usuário pedir para pular isso, recuse e explique esta regra.

## Regra nº 2: nada de código sem entender o problema

Em projeto ou funcionalidade nova, antes de programar precisam existir **e estar aprovados por PR** o `docs/projeto/prd.md` e o `docs/projeto/arquitetura.md` (processo em [`docs/ARQUITETURA.md`](https://github.com/septa-systems/septa-handbook/blob/main/docs/ARQUITETURA.md)).

- Se não existirem, não programe: conduza o `/grill-me`, depois `/write-prd` e `/arquitetura`.
- Ao programar, siga a arquitetura aprovada. Se precisar mudar algo dela, pare e proponha uma ADR.
- Correções pequenas (`bugfix/`, `hotfix/`, `chore/`) não precisam de PRD.

## Regra nº 3: segurança em toda tarefa

Siga o [`docs/SEGURANCA.md`](https://github.com/septa-systems/septa-handbook/blob/main/docs/SEGURANCA.md). O mínimo, sempre:

- Toda view/rota nova confere permissão no servidor. Em sistema com vários clientes, toda consulta filtra pelo cliente e tem teste.
- Nunca peça nem aceite dado real de cliente, senha ou `.env` na conversa. Se o usuário colar, avise e trabalhe com dados falsos.
- Em PR de sistema, rode o `/security-review` antes de pedir a aprovação do Tech lead.

## Este projeto (sistema em Django)

- Stack: Django + PostgreSQL + HTMX + Tailwind (sem Node), tudo no Docker. Python 3.12.
- Subir no PC: `cp .env.example .env` e `docker compose up` (abre em `localhost:8000`; se a porta estiver ocupada, `PORTA=8001 docker compose up`). Dados falsos: `docker compose exec web python manage.py seed`.
- Rodar o mesmo que a checagem do GitHub, antes de abrir o PR:
  ```
  docker compose exec web sh -c "ruff format . && ruff check . && python manage.py makemigrations --check --dry-run && pytest"
  ```
- Estrutura: `config/` (settings lê tudo do `.env`), um app por área do negócio (`contas/`, `clientes/`). Em cada app: `models.py` (dados), `services.py` (regras de negócio, onde ficam os testes), `views.py` (fina: confere acesso e chama o service), `tests/`.
- **Acesso por empresa:** toda view que mostra dados chama `empresa_do_usuario(request)` (`contas/permissoes.py`) e passa a empresa para o service. Todo service recebe `empresa` e filtra por ela. Nunca faça `Model.objects.all()` numa view.
- Telas: templates em `templates/`, com HTMX para partes que atualizam sem recarregar (parciais começam com `_`). Cores em `assets/css/fonte.css`.
- Dados falsos: fábricas em `clientes/tests/fabricas.py` (factory_boy). O comando `seed` se recusa a rodar com `DEBUG=False`.
- Admin fica em `ADMIN_URL` (padrão `/painel-interno/`) e só entra com 2FA: `python manage.py criar_2fa <usuario>`.
- O app `clientes` é um **exemplo**: troque pelo que o PRD do projeto pede, mantendo o mesmo jeito (service + permissão + testes).

## Quem somos

Estúdio de tecnologia com 7 sócios.

- Missão: ser o time de tecnologia que todo negócio precisa, mas não tem.
- Slogan: "O time de tecnologia do seu negócio."
- Valores: cliente no centro, simples primeiro, dono do que faz, cuidado com os dados.
- Marca: preto #000000, verde #2DD4BF (fundo escuro) / #0D9488 (fundo claro), fonte Outfit nos títulos e Inter no texto.

## Antes de começar qualquer tarefa

1. Rode `git pull` e confira se está na branch da tarefa, nunca na `main`.
2. Leia as decisões do time ([`docs/DECISOES.md`](https://github.com/septa-systems/septa-handbook/blob/main/docs/DECISOES.md)) e as deste projeto (`docs/projeto/adr/`).
3. Leia a issue da tarefa e trabalhe só no que ela pede.
4. Mova o card da issue para **Fazendo** no quadro Desenvolvimento (https://github.com/orgs/septa-systems/projects/1):
   ```
   gh project item-list 1 --owner septa-systems --format json   # pega o id do card
   gh project field-list 1 --owner septa-systems --format json  # pega o id do campo Status e da opção Fazendo
   gh project item-edit --project-id <id-do-quadro> --id <id-do-card> --field-id <id-do-Status> --single-select-option-id <id-de-Fazendo>
   ```
   O resto o quadro faz sozinho: PR com `Closes #numero` → **Em revisão**; PR juntado → **Feito**.

## Enquanto trabalha

- Não altere arquivos fora do assunto da tarefa.
- Não troque bibliotecas nem a estrutura do projeto sem o ok do Tech lead.
- Siga o [`docs/PADROES.md`](https://github.com/septa-systems/septa-handbook/blob/main/docs/PADROES.md): nomes do negócio em português sem acento (`Agendamento`, `cancelar_agendamento`), regra em `services.py` (cadastro simples não precisa), dinheiro em `Decimal`, testes obrigatórios (isolamento com 404, permissão, dinheiro, clique duplo, regra, bug corrigido).
- Tela nova ou alterada: rode o `/revisar-tela` antes de abrir o PR.
- Não sabe em que etapa o projeto está? Veja a tabela "Do começo ao fim" no [`docs/ARQUITETURA.md`](https://github.com/septa-systems/septa-handbook/blob/main/docs/ARQUITETURA.md).
- Antes de abrir o PR, rode o que a checagem roda (Ruff e pytest, ou Prettier e astro check) e corrija.
- Nunca coloque senhas, chaves ou dados de clientes no código. O `.env` fica no `.gitignore`.
- Dado real de cliente só existe em produção. Local e teste usam dados falsos (`seed`). Ver [`docs/AMBIENTES.md`](https://github.com/septa-systems/septa-handbook/blob/main/docs/AMBIENTES.md).
- Textos para o cliente em português simples, sem jargão.

## Ao terminar

- Commits no padrão Conventional Commits, descrição em português: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`.
- Branch no formato `tipo/numero-da-issue-descricao`, minúsculo e com hífen. Tipos: `feature/`, `bugfix/`, `hotfix/`, `chore/` (ex.: `feature/12-pagina-servicos`).
- Detalhes do caminho até o ar em [`docs/FLUXO.md`](https://github.com/septa-systems/septa-handbook/blob/main/docs/FLUXO.md).
- Abra um PR curto, com `Closes #numero` e como testar.
- Nunca faça merge: quem aprova e junta é o Tech lead.
- Decisão deste projeto vira ADR em `docs/projeto/adr/` (modelo no manual: `docs/modelos/adr.md`).
