---
name: arquitetura
description: A partir do PRD aprovado, monta o documento de arquitetura (C4, restrições, apps, modelo de domínio, segurança, cenários de qualidade, riscos) e as ADRs em docs/projeto/. Use quando o usuário digitar /arquitetura ou pedir para pensar a arquitetura de um projeto. Fase 3 do docs/ARQUITETURA.md da Septa.
---

Monte a arquitetura do projeto seguindo os fundamentos do `docs/ARQUITETURA.md` da Septa.

1. Leia `docs/projeto/prd.md`. Se não existir, pare e sugira `/grill-me` e `/write-prd` antes.
2. Leia `docs/DECISOES.md` e a stack padrão (Django + PostgreSQL + Docker + HTMX, fila de saída + worker para avisos). Só fuja dela com motivo forte, registrado em ADR.
3. Discuta com o usuário, uma pergunta por vez e com recomendação, o que o PRD não responde: restrições (prazo, orçamento, hospedagem, sistema que o cliente já usa), quem pode ver o quê, o que nunca pode ser apagado, as multiplicidades que o cliente ainda não confirmou.
4. Escreva `docs/projeto/arquitetura.md` seguindo `docs/modelos/arquitetura.md`:
   - C1 sem tecnologia, com tipo em cada caixa e verbo nas setas; C2 com nome + tecnologia + o que faz, e o protocolo nas setas
   - Restrições (técnicas, do time, do projeto)
   - Apps Django por área do negócio (monólito modular, com a regra de import entre apps)
   - Modelo de domínio em Mermaid `classDiagram`, com multiplicidade nas duas pontas, seguindo os 5 passos da fase 3
   - Fluxos principais
   - Segurança e LGPD (obrigatório)
   - Requisitos de qualidade como cenários estímulo → resposta → medida, e riscos
5. Para cada decisão que custa caro desfazer e afeta boa parte do sistema, crie `docs/projeto/adr/NNNN-nome.md` seguindo `docs/modelos/adr.md`, sempre com "O que sacrificamos".
6. Antes de entregar, confira o checklist da fase 4 do `docs/ARQUITETURA.md`.

Regras:

- Simples primeiro (KISS/YAGNI): não proponha o que o PRD não pede. Sem Celery/Redis, cache ou microsserviço sem necessidade medida.
- Os mesmos nomes do glossário no C1, no domínio e no código.
- Não escreva código do sistema. Este passo termina no documento.
- O documento entra por PR e o Tech lead aprova antes de qualquer código. Sugira o próximo passo: fatiar o PRD em issues.
