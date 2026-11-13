---
name: revisar-tela
description: Revisa uma tela (ou o fluxo de telas) com as 10 heurísticas de Nielsen e devolve os problemas com severidade. Use quando o usuário digitar /revisar-tela, pedir revisão de UX/usabilidade ou antes de entregar uma tela nova. Etapa 7 do docs/ARQUITETURA.md da Septa.
---

Revise a tela ou o fluxo que o usuário indicar (template, componente, rota ou PR) com as 10 heurísticas de Nielsen, como o usuário final usaria: no celular primeiro.

1. Descubra a **tarefa principal** da tela e quem a faz (veja o PRD em `docs/projeto/prd.md`, se existir: papéis, aparelho, meta de usabilidade).
2. Leia o código da tela (template, view, form, JS/HTMX) e siga o fluxo do começo ao fim, incluindo os caminhos de erro.
3. Confira cada heurística:

| #   | Heurística                | O que procurar                                                                           |
| --- | ------------------------- | ---------------------------------------------------------------------------------------- |
| 1   | Visibilidade do estado    | botão que envia mostra "Enviando..." e trava? Confirmação clara depois?                  |
| 2   | Linguagem do mundo real   | palavras do cliente (glossário do PRD), sem "Erro 409" nem jargão                        |
| 3   | Controle e liberdade      | dá para voltar, corrigir e cancelar sem recomeçar nem perder o que digitou?              |
| 4   | Consistência              | mesmo rótulo = mesmo comportamento no sistema todo                                       |
| 5   | Prevenção de erros        | opção inválida bloqueada antes (horário ocupado, data passada), e não recusada só no fim |
| 6   | Reconhecer, não memorizar | opções e dados na tela, sem pedir código ou coisa que a pessoa tenha que lembrar         |
| 7   | Flexibilidade             | atalho para quem usa sempre (ex.: repetir o último agendamento)                          |
| 8   | Estética e minimalismo    | só o necessário para a tarefa                                                            |
| 9   | Recuperação de erros      | a mensagem diz o que houve, por quê e como resolver                                      |
| 10  | Ajuda                     | instrução curta no ponto em que a pessoa precisa                                         |

Confira também o mínimo do `docs/PADROES.md` seção 6: `<label>` em todo campo, `alt` em imagem, contraste, uso só com o teclado, toque confortável no celular.

4. Responda com uma tabela, da mais grave para a menos grave:

| Severidade | Heurística | Onde (arquivo:linha) | Problema | Sugestão |
| ---------- | ---------- | -------------------- | -------- | -------- |

Severidade: **Crítico** = impede concluir a tarefa principal · **Alto** = erro frequente ou perda de dados · **Médio** = mais esforço, mas tem alternativa · **Baixo** = incômodo pontual.

Regras:

- Decida pela frequência, pelo impacto e pelo contexto, e não por gosto pessoal.
- Não altere código sem o usuário pedir. Se pedir, corrija primeiro os críticos e os altos.
- Esta revisão acha problemas possíveis. Antes do lançamento, ainda vale o teste com umas 5 pessoas reais (`docs/PADROES.md` seção 6).
