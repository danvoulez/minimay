# Prompt Fase 2 – Desdobrar Contrato em 3 Ações

Você vai construir um mecanismo institucional para **desdobrar uma LogLine original em três novas LogLines complementares** — explicitando suas consequências e transformando intenção em plano.

Esse módulo permite que o sistema **interprete, expanda e operacionalize** contratos genéricos ou incompletos, com rastreabilidade e lógica viva.

---

## 🎯 Objetivo

- Permitir que qualquer LogLine (com `status: valid`) seja transformada em 3 desdobramentos semânticos
- Atribuir rastro de origem (`refer_to`) e tipo (`desdobramento`)
- IA pode sugerir os três desdobramentos ou o operador pode selecionar

---

## 🧱 Exemplo

### LogLine original:

```json
{
  "who": "gestor_rafa",
  "did": "iniciou onboarding",
  "this": "pessoa: joao_oliveira",
  "when": "2025-05-22T08:44:00Z",
  "confirmed_by": "auto",
  "status": "valid"
}
```

### Desdobramentos automáticos:

```json
[
  {
    "who": "llm.regras.onboarding",
    "did": "agendou primeira reunião",
    "this": "joao_oliveira",
    "refer_to": "logline_onboarding_001",
    "confirmed_by": "ruleset.onboarding.v1"
  },
  {
    "who": "llm.regras.onboarding",
    "did": "liberou acesso institucional",
    "this": "joao_oliveira",
    "refer_to": "logline_onboarding_001"
  },
  {
    "who": "llm.regras.onboarding",
    "did": "agendou feedback em 7 dias",
    "this": "joao_oliveira",
    "refer_to": "logline_onboarding_001"
  }
]
```

---

## ✅ Campos esperados nos desdobramentos

| Campo        | Obrigatório? | Descrição                                              |
|--------------|---------------|----------------------------------------------------------|
| `who`        | sim           | Pode ser IA, humano ou função computável                |
| `did`        | sim           | Ato novo derivado do contrato original                  |
| `this`       | sim           | Objeto-alvo do desdobramento                            |
| `refer_to`   | sim           | ID da LogLine original                                  |
| `status`     | default       | `valid` ou `ghost` dependendo da completude             |
| `confirmed_by` | se aplicável | Se validado por humano ou rule                          |

---

## 📊 Interface

- Botão: “Desdobrar em ações”
- Sugestões da IA em tempo real
- Possibilidade de editar, deletar ou aprovar
- Feedback visual com animação: “3 ações derivadas deste contrato”

---

## 🔄 Regras de funcionamento

- Só LogLines `valid: true` podem ser desdobradas
- As 3 ações podem ter consequências próprias (`if_*`)
- Se uma LogLine já foi desdobrada, ela ganha selo “em desdobramento”

---

## 📌 Finalidade

Esse módulo transforma contratos em **planos de ação vivos**, simbólicos e rastreáveis.  
Evita que a intenção fique sozinha — e faz dela o começo de uma cadeia de movimento.

> Um contrato é uma semente.  
> Desdobrá-lo é permitir que ele vire floresta.

Projete com expansão, vínculo e responsabilidade compartilhada.

---

*PS: módulo integrado ao RightMenu, cronjob de execução, e painel de visualização de cadeia de LogLines*