# Prompt 14 – Agente Institucional: Agent.14 (Guardião de Conflitos e Condições)

Você vai construir o **Agent.14**, responsável por **detectar conflitos lógicos, simbólicos ou operacionais entre LogLines**,  
e por aplicar as **condições de execução ou bloqueio institucional** de forma preventiva e auditável.

---

## 🎯 Objetivo

- Observar a linha do tempo institucional e detectar:
  - Contradições entre ações (`did`)
  - Falta de consequência após evento crítico
  - Condições descumpridas para execução de `if_*`
  - Ghosts que se sobrepõem a registros válidos
- Marcar LogLines conflitantes
- Gerar LogLine `did: detectou_conflito` com detalhes

---

## 🧱 Exemplo de conflito detectado

```json
{
  "who": "agent.14",
  "did": "detectou_conflito",
  "this": "venda_293 X cancelamento_293",
  "when": "2025-05-23T11:10:00Z",
  "status": "valid",
  "refer_to": ["logline_venda", "logline_cancelamento"],
  "severity": "alta",
  "type": "contradição temporal"
}
```

---

## ✅ Tipos de conflito que ele identifica

| Tipo                         | Exemplo prático                                      |
|------------------------------|-------------------------------------------------------|
| `duplicação_institucional`   | Duas LogLines dizendo que a mesma entrega ocorreu    |
| `fantasma_vs_realidade`      | Ghost registrando falha depois de contrato validado  |
| `condição_descumprida`       | Executar `if_ok` antes da testemunha confirmar       |
| `intenção_conflitante`       | Um `did: cancelou` e um `did: confirmou` em sequência|
| `suspensão_temporal`         | Duas ações simultâneas sobre o mesmo objeto (`this`) |

---

## 🛡️ Comportamento

- Não apaga nem corrige: apenas registra o conflito
- Pode suspender temporariamente a execução de Agent.13 para `refer_to`
- Pode sugerir ação no RightMenu
- Gera LogLine própria para cada conflito
- Integra com painel de auditoria e cronjob

---

## 📊 Campos esperados

| Campo         | Descrição                                   |
|---------------|-----------------------------------------------|
| `who`         | Sempre `agent.14`                             |
| `did`         | `"detectou_conflito"`                         |
| `refer_to`    | IDs das LogLines conflitantes                 |
| `type`        | Tipo de conflito                              |
| `severity`    | `baixa`, `moderada`, `alta`, `crítica`        |
| `status`      | Sempre `valid`                                |

---

## 📌 Finalidade

Agent.14 é o **guardião das contradições institucionais**.  
Ele observa, não julga — mas registra, alerta e protege o fluxo semântico do sistema.

> Onde há dúvida, há sinal.  
> Onde há conflito, há dado.  
> Onde há rastro, pode haver correção.

Projete com vigilância simbólica, silêncio respeitoso e poder institucional latente.

---

*PS: Agent.14 não impede nada — mas revela tudo.*