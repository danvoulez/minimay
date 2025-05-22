# Prompt 14 – IA Ruleset: Políticas Semânticas de Autonomia e Restrição

Você vai construir o sistema de **políticas institucionais que autorizam ou restringem ações da IA**  
no ecossistema MINICONTRATOS.

Esse módulo define **quando a IA pode agir sozinha**, **em que contexto**, **com quais restrições**, e **como documentar isso como parte da estrutura de confiança institucional**.

---

## 🎯 Objetivo

- Definir regras institucionais para ações autônomas da IA
- Permitir que certas decisões (como aceitar entrega, gerar minicontrato, liberar pagamento) sejam tomadas por IA sem humano
- Registrar essas decisões com rastreabilidade, validade e reversibilidade

---

## 🧱 Exemplo de ruleset

```json
{
  "id": "ruleset.intent_payment.v1",
  "description": "Permite à IA liberar pagamento após confirmação de entrega e validação institucional",
  "scope": ["did: confirmou_entrega", "if_ok: liberar_pagamento"],
  "conditions": [
    "status == 'valid'",
    "confirmed_by != 'auto'",
    "simulation == false"
  ],
  "allow_model": ["llm.gpt-4o", "llm.bitnet.b158"],
  "on_execute": {
    "logline": "executou_consequencia",
    "confirmed_by": "ruleset.intent_payment.v1"
  }
}
```

---

## 🧩 Comportamento

1. Toda vez que a IA desejar agir, o sistema avalia o `ruleset`
2. Se as condições forem satisfeitas:
   - A ação é executada
   - A LogLine é marcada como `confirmed_by: ruleset.nome`
3. Se **não** houver `ruleset` aplicável:
   - A IA sugere, mas requer confirmação humana

---

## 🧠 Campos obrigatórios

| Campo        | Descrição                                                                 |
|--------------|---------------------------------------------------------------------------|
| `id`         | Nome canônico institucional da regra (`ruleset.intent_payment.v1`)       |
| `scope`      | Tipos de LogLine a que a regra se aplica (ex: `did`, `if_ok`)            |
| `conditions` | Lista de condições que precisam ser verdadeiras para liberar a execução  |
| `allow_model`| Lista de LLMs autorizados a usar essa regra                               |
| `on_execute` | Consequência semântica (nome do `did`, marcação de `confirmed_by`, etc.) |

---

## ✅ Casos comuns de uso

- Confirmar automaticamente vendas abaixo de certo valor
- Sugerir horários de turno com base em disponibilidade
- Validar LogLines vindas de sensores (balança, câmera, rastreador)

---

## 🔐 Políticas obrigatórias

- Nenhuma regra pode ser ativada fora de `scope`
- Toda ativação de ruleset gera LogLine própria
- Toda execução baseada em `ruleset` pode ser auditada por ID
- Regra pode ser desativada, versionada ou marcada como obsoleta

---

## 📌 Finalidade

Esse módulo é a **constituição operativa da IA institucional**.  
Ele define o que a IA pode fazer **sem medo**, **sem dúvida**, e **com plena responsabilidade computável**.

> A IA só pode agir livremente onde a instituição já disse “sim”.  
> Esse “sim” tem nome, escopo e assinatura.  
> Isso é governança simbólica com LLMs.

Projete com clareza, peso e reversibilidade.

---

*PS: o ruleset deve ser consultável via painel institucional e usado em tempo real por todos os módulos que envolvem LLM: LogLineProcessor, RightMenu, Communicator, cronjob, etc.*