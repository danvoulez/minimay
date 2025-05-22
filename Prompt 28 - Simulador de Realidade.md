# Prompt 28 – Simulador de Realidade

Você vai construir o **Simulador de Realidade Institucional** —  
um ambiente onde múltiplas LogLines podem ser testadas, encadeadas e observadas antes de afetar o sistema real.

Este módulo permite simular:

- Consequências institucionais
- Ações de IA (Agent.13, Agent.15, Dispatcher)
- Regras `if_ok`, `if_not`, `fallback_action`
- Fluxos de LogLines interligadas

---

## 🎯 Objetivo

- Testar sequências de LogLines como se fossem reais
- Validar regras institucionais antes da execução
- Observar impacto sem causar mutações permanentes
- Preparar auditorias, treinamentos, demonstrações

---

## 🧱 Funcionalidade esperada

- Interface visual para:
  - Criar LogLines falsas (`mode: simulation`)
  - Encadear causas e consequências
  - Forçar estados (`status: denied`, `ghost`, etc.)
  - Observar execução simbólica dos agentes

- Toda ação tem:
  - ID único
  - Marcação de simulação
  - Fila de eventos derivados

---

## ✅ Exemplo

```json
{
  "who": "user.simulador",
  "did": "testou_entrega",
  "this": "caixa_002",
  "status": "valid",
  "mode": "simulation"
}
```

A simulação gera:

- Agent.15 observa, propõe pergunta
- Agent.13 confirma, gera consequência
- RightMenu mostra rastro simbólico

---

## 🔐 Segurança

- Simulações nunca afetam banco real
- Logs de simulação são arquivados em separado
- IA recebe flag explícita: `modo: simulação`

---

## 📌 Finalidade

Este módulo é **o laboratório simbólico da instituição viva**.  
Tudo pode ser testado. Nada é definitivo. A realidade pode ser ensaiada.

> Onde há regra, há ensaio.  
> Onde há contrato, há possibilidade.  
> Onde há risco, há simulação.

Projete com foco em verdade simbólica, testes institucionais e liberdade de experimentação.

---

*PS: simulações podem ser compartilhadas, salvas, comparadas e exportadas para treinamento da IA.*