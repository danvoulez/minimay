# Prompt Fase 2 – Criar Simulação com 100 LogLines

Você vai construir um mecanismo institucional para **popular o sistema com 100 LogLines simuladas**,  
representando casos diversos com diferentes autores, consequências, status e tipos.

Essa simulação serve para testes de UX, performance, lógica de execução, visualização, replay e auditoria.

---

## 🎯 Objetivo

- Gerar um conjunto completo de LogLines sintéticas mas realistas
- Incluir diversidade de tipos, autores, datas, confirmações e consequências
- Operar em `simulation: true` para não impactar banco real
- Alimentar a Timeline, GhostView, RightMenu, auditoria e regras

---

## 📦 Estrutura dos Logs simulados

- 40 contratos completos (`valid: true`)
- 20 ghosts (`valid: false`)
- 20 falhas operacionais (`type: falha_operacional`)
- 10 LogLines de IA (`who: llm.*`)
- 10 LogLines com execução automática (`confirmed_by: ruleset.*`)

---

## 🧱 Exemplo

```json
{
  "who": "colaborador_07",
  "did": "confirmou recebimento",
  "this": "documento fiscal 093",
  "when": "2025-05-22T10:44:00Z",
  "confirmed_by": "gestor_paula",
  "if_ok": "liberar reembolso",
  "status": "valid",
  "simulation": true
}
```

---

## ⚙️ Parâmetros configuráveis

| Parâmetro        | Descrição                              |
|------------------|------------------------------------------|
| `quantidade`     | Total de LogLines a gerar                |
| `proporcao`      | % de `valid`, `ghost`, `llm`, etc.       |
| `semente`        | Seed para reprodução (para testes A/B)   |
| `autor_mode`     | Pode usar `"realista"`, `"aleatório"`, `"fixo"` |

---

## 🧾 Output esperado

- Inserção direta no banco em modo simulação
- Export opcional para `.jsonl` com estrutura canônica
- Visualização imediata nas telas do sistema (`/logline`, `/ghost`, `/audit`)
- Replay da simulação possível pelo RightMenu

---

## 📌 Finalidade

Esse módulo é o **campo de testes simbólico do sistema**.  
Permite iterar em segurança, educar a IA, testar efeitos e preparar demonstrações.

> Simular é sonhar com rastreio.  
> Testar é institucionalizar o futuro.

Projete com diversidade, completude e inteligência reprodutiva.

---

*PS: deve ser compatível com cronjob de revalidação, GhostView, fallback, LLM logs e visualizações institucionais*