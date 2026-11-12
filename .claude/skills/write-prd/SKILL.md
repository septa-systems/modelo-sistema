---
name: write-prd
description: Transforma a conversa (de preferência depois do /grill-me) num PRD, o documento do que vai ser feito, salvo em docs/projeto/prd.md. Use quando o usuário digitar /write-prd ou pedir para escrever um PRD. Fase 2 do docs/ARQUITETURA.md da Septa.
---

Escreva o PRD (documento de requisitos) do projeto ou funcionalidade discutida.

1. Se ainda não houve entrevista nesta conversa, peça uma descrição detalhada do problema e faça perguntas uma por vez, como no /grill-me, até ficar claro.
2. Leia `docs/projeto/entrevista.md` se existir, e explore o código do projeto.
3. Antes de escrever, mostre a lista de módulos/apps que pretende criar ou mudar e espere o usuário aprovar. Prefira módulos profundos: interface pequena e simples, com bastante lógica dentro, fácil de testar por fora.
4. Siga o modelo `docs/modelos/prd.md` do manual da Septa (https://github.com/septa-systems/septa-handbook). Salve em `docs/projeto/prd.md` (projeto novo) ou `docs/projeto/prd-<funcionalidade>.md` (funcionalidade nova num projeto que já existe).

Regras:

- Use só o que foi decidido na conversa; não invente requisitos.
- O glossário usa as palavras do cliente; elas viram nomes no código.
- Não faça commit sem o usuário pedir. Quando pedir, siga o `docs/FLUXO.md` (branch, PR, aprovação do Tech lead).
- Depois de salvo, diga o caminho do arquivo e sugira o próximo passo: `/arquitetura`.
