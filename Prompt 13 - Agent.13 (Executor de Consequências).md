# Prompt 13 – Agente Institucional: Agent.13 (Executor de Consequências)

Você vai criar um agente interno do sistema chamado **Agent.13**, responsável por **executar consequências** especificadas nos campos `if_ok`, `if_doubt`, `if_not` das LogLines que foram validadas.

Esse agente é **autônomo, auditável e reversível** — ele transforma registros em ações, mas sempre deixa rastro simbólico.

---

## 🎯 Objetivo

- Monitorar LogLines com `status: valid` e consequências não executadas
- Executar a ação correspondente com base na política definida
- Gerar nova LogLine de execução (`did: executou_consequencia`)
- Atuar com base em `ruleset`, fallback ou aprovação manual

---

## 🧱 Exemplo

### LogLine original:

```json
{
  "who": "colaborador_05",
  "did": "confirmou entrega",
  "this": "pedido_344",
  "status": "valid",
  "if_ok": "liberar pagamento",
  "confirmed_by": "gestor_daniel"
}
```

### LogLine gerada por Agent.13:

```json
{
  "who": "agent.13",
  "did": "executou_consequencia",
  "this": "liberar pagamento para pedido_344",
  "refer_to": "logline_id_origem",
  "when": "2025-05-23T09:20:00Z",
  "confirmed_by": "ruleset.intent_payment.v1",
  "status": "valid"
}
```

---

## ✅ Regras operacionais

- Só age sobre LogLines com `status: valid` e pelo menos um `if_*`
- Só executa `if_ok` se status simbólico do sistema for positivo (sem pendência ou veto)
- Se múltiplos `if_*` forem possíveis, exige resolução manual ou regra explícita
- Pode operar em modo simulação
- Todas as ações são reversíveis com `did: desfez_consequência`

---

## 🔄 Campos gerados

| Campo          | Descrição                                         |
|----------------|---------------------------------------------------|
| `who`          | Sempre `agent.13`                                 |
| `did`          | Ação simbólica derivada de `if_*`                 |
| `refer_to`     | ID da LogLine original                            |
| `confirmed_by` | Pode ser humano, `ruleset`, ou `auto`             |
| `status`       | `valid` ou `denied`                               |

---

## 🧠 Integrações

- Cronjob de verificação
- LogLineProcessor
- RightMenu
- Replay institucional de ações

---

## 📌 Finalidade

Agent.13 é o executor simbólico da instituição.  
Ele transforma intenção em ato. Registro em gesto.  
Mas nunca age no escuro: **tudo que ele faz é documentado, reversível e institucional**.

> Toda consequência precisa de um executor.  
> E todo executor precisa de limite, memória e reverência.

Projete com responsabilidade semântica, limites auditáveis e liberdade computável.

---

*PS: Agent.13 pode ser suspenso, simulado ou auditado por outro agente institucional*