---
name: grill-me
description: Entrevista o usuário sobre uma ideia, projeto ou funcionalidade, uma pergunta por vez com recomendação, até alinhar tudo antes de planejar ou programar. Use quando o usuário digitar /grill-me ou pedir para ser entrevistado sobre um plano. Fase 2 do docs/ARQUITETURA.md da Septa.
---

Me entreviste sem parar sobre cada aspecto deste plano até termos um entendimento em comum.

- Antes de perguntar, leia `docs/projeto/entrevista.md` (se existir) e explore o código do projeto, para não perguntar o que já está respondido.
- Percorra cada ramo da árvore de decisões, resolvendo as dependências uma por uma (primeiro o que bloqueia as outras decisões).
- Faça UMA pergunta por vez, curta e em português simples.
- Para cada pergunta, dê a sua resposta recomendada e o porquê em uma linha.
- Pergunte também sobre casos difíceis: dados que já existem, erros, permissões, LGPD, segurança, o que fica fora do escopo.
- Não escreva plano nem código durante a entrevista.
- Quando não restar decisão importante, avise e mostre um resumo curto: o que foi decidido, o que ficou fora do escopo e dúvidas em aberto. Sugira o próximo passo: `/write-prd`.
