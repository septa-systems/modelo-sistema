---
name: arquitetura
description: A partir do PRD aprovado, monta o documento de arquitetura (C4, apps, modelo de dados, segurança, riscos) e as ADRs em docs/projeto/. Use quando o usuário digitar /arquitetura ou pedir para pensar a arquitetura de um projeto. Fase 3 do docs/ARQUITETURA.md da Septa.
---

Monte a arquitetura do projeto seguindo os fundamentos do `docs/ARQUITETURA.md` da Septa.

1. Leia `docs/projeto/prd.md`. Se não existir, pare e sugira `/grill-me` e `/write-prd` antes.
2. Leia `docs/DECISOES.md` e a stack padrão (Django + PostgreSQL + Docker + HTMX). Só fuja dela com motivo forte, registrado em ADR.
3. Discuta com o usuário, uma pergunta por vez e com recomendação, as decisões que o PRD não responde (ex.: precisa de tarefa em segundo plano? quem pode ver o quê? o que nunca pode ser apagado?).
4. Escreva `docs/projeto/arquitetura.md` seguindo `docs/modelos/arquitetura.md`:
   - C4 Contexto e Containers em Mermaid
   - Apps Django por área do negócio (monólito primeiro, nada de microserviços)
   - Modelo de dados em Mermaid `erDiagram`
   - Fluxos principais
   - Segurança e LGPD (obrigatório)
   - Requisitos de qualidade e riscos
5. Para cada decisão importante, crie `docs/projeto/adr/NNNN-nome.md` seguindo `docs/modelos/adr.md`.

Regras:

- Simples primeiro (KISS/YAGNI): não proponha o que o PRD não pede.
- Regra de negócio em `services.py`, view fina, nomes com as palavras do glossário.
- Não escreva código do sistema. Este passo termina no documento.
- O documento entra por PR e o Tech lead aprova antes de qualquer código. Sugira o próximo passo: fatiar o PRD em issues.
