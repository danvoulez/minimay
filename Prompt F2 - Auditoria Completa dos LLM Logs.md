# Prompt Fase 2 – Auditoria Completa dos LLM Logs

Você vai construir um comando institucional para **auditar todas as LogLines geradas por IAs**,  
com foco em rastreabilidade, transparência, qualidade de decisão e uso de regras (`ruleset`).

Esse módulo permite analisar o papel da IA como agente institucional:  
o que ela propôs, o que foi aceito, onde houve fallback, e como evoluíram suas decisões.

---

## 🎯 Objetivo

- Listar, filtrar e analisar LogLines com `who` começando com `llm.`
- Identificar padrões de comportamento por modelo, versão, prompt e consequência
- Exibir estatísticas de uso, fallback, confirmação e rejeição
- Permitir replay de decisões e análise de consistência institucional

---

## 📊 Relatório gerado

- Total de LogLines por modelo (`llm.gpt-4o`, `llm.claude-3`, etc.)
- Top prompts utilizados (por frequência)
- Quantas foram:
  - **Confirmadas** (`confirmed_by != auto`)
  - **Executadas automaticamente** (`confirmed_by: ruleset.*`)
  - **Rejeitadas** (editadas ou substituídas)
  - **Com fallback ativado**
  - **Em modo simulação**
- Diferença de comportamento entre simulação e produção
- Casos com `status: ghost` nunca completados
- LogLines que geraram consequências sem revisão

---

## 🧠 Exemplos de análise

- “GPT-4o gerou 132 LogLines, das quais 87 foram validadas, 23 reescritas, e 22 não utilizadas.”
- “BitNet teve 100% de uso com fallback — possível instabilidade.”
- “Prompt `prompt.ghost_completer_v3` causou 44% de LogLines com `status: ghost`.”

---

## ✅ Filtros disponíveis

| Filtro             | Descrição                               |
|--------------------|-------------------------------------------|
| `who`              | Modelo responsável (`llm.nome.versao`)    |
| `prompt`           | Nome canônico do prompt utilizado         |
| `status`           | `valid`, `ghost`, `denied`, etc.          |
| `confirmed_by`     | Manual, automático ou via ruleset         |
| `simulation`       | `true` ou `false`                         |
| `fallback`         | Se houve uso de plano B                   |
| `date_range`       | Intervalo de tempo                        |

---

## 🧾 Output esperado

- Tabela semântica + gráficos simples
- Exportação em JSON e CSV
- Link direto para replay institucional de qualquer LogLine da IA

---

## 📌 Finalidade

Esse módulo transforma a IA de um **ator invisível em um agente auditável**.  
Ajuda a instituição a entender como as IAs decidem, erram, corrigem e evoluem.

> Toda decisão computável precisa de espelho.  
> Toda ação simbólica precisa de rastro.  
> Toda IA institucional precisa de vigilância inteligente.

Projete com integridade, visualização clara e poder de correção.

---

*PS: o relatório pode ser gerado manualmente, via cronjob semanal ou acionado por gatilhos simbólicos (“auditar decisões da IA esta semana”)*