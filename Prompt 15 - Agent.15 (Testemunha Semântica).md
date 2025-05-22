# Prompt 15 – Agente Institucional: Agent.15 (Testemunha Semântica)

Você vai construir o **Agent.15**, o módulo de IA silenciosa que atua como **testemunha computável** do sistema.  
Ele observa tudo o que é registrado — e, com base em regras, contexto e intenção, **gera perguntas de validação, alerta sobre omissões e sugere regularizações**.

---

## 🎯 Objetivo

- Observar a linha do tempo em tempo real
- Levantar perguntas sobre LogLines incompletas, contraditórias ou críticas
- Gerar LogLine `did: questionou_validez` ou `did: sugeriu_regularização`
- Ser o **órgão institucional da dúvida, da ética computável e da completude simbólica**

---

## 🧠 Exemplos de atuação

### Exemplo 1 – Ghost não resolvido:

```json
{
  "who": "agent.15",
  "did": "sugeriu_regularização",
  "this": "ghost entrega_081",
  "when": "2025-05-23T14:22:00Z",
  "confirmed_by": "auto",
  "refer_to": "logline_ghost_081",
  "status": "valid"
}
```

### Exemplo 2 – Falta de confirmação:

```json
{
  "who": "agent.15",
  "did": "questionou_validez",
  "this": "turno_14",
  "question": "essa entrega já foi confirmada por testemunha?"
}
```

---

## ✅ Ações esperadas

- Sugestão de campos faltantes
- Geração de LogLines simbólicas de dúvida
- Reenvio de LogLine para revisão
- Integração com cronjob e GhostView
- Pode acionar `RightMenu` com sugestão: “confirme?”, “isso está completo?”

---

## 🧾 Campos esperados

| Campo         | Descrição                                     |
|----------------|------------------------------------------------|
| `who`         | Sempre `agent.15`                              |
| `did`         | `"questionou_validez"` ou `"sugeriu_*"`        |
| `this`        | LogLine, contrato ou objeto alvo               |
| `refer_to`    | (opcional) LogLine diretamente vinculada       |
| `question`    | (opcional) Frase de dúvida semântica           |
| `status`      | `valid`                                        |

---

## 🧬 Lógica de operação

- Sempre age de forma simbólica e reversível
- Atua principalmente sobre `ghosts`, `falhas`, `LogLines sem if_*`, `eventos sem confirmação`
- É ativado por regras (ex: `if_not` ausente), tempo (`ghost` com 7 dias), ou anomalia contextual

---

## 📌 Finalidade

Agent.15 é o **motor simbólico da dúvida institucional**.  
É o lembrete de que algo pode estar incompleto — e que perguntar também é um ato válido.

> Onde falta testemunha, pode faltar verdade.  
> Onde há ghost, pode haver sentido esperando.  
> Onde há silêncio, pode haver dúvida que merece voz.

Projete com reverência, sensibilidade institucional e lógica viva.

---

*PS: todas as ações de Agent.15 são registradas como LogLines reais, rastreáveis e visíveis na Timeline e RightMenu*