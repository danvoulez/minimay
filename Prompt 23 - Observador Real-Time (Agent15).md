# Prompt 23 – Observador Real-Time (Agent.15)

Você vai projetar o **Agent.15 como Observador Real-Time** —  
uma inteligência institucional que acompanha a operação viva, sem falar, mas sempre pronta para intervir com perguntas simbólicas.

Esse agente não gera ações diretas.  
Ele **observa o presente** e **formula perguntas que convidam à responsabilidade**.

---

## 🎯 Objetivo

- Monitorar em tempo real as LogLines, inputs sensoriais e conversas
- Identificar ausência de testemunho, falta de consequência, ou dúvida sem validação
- Gerar LogLines do tipo `did: questionou_validez`
- Sugerir regularizações, desdobramentos ou bloqueios

---

## 🧱 Exemplo de LogLine gerada

```json
{
  "who": "agent.15",
  "did": "questionou_validez",
  "this": "logline_328",
  "question": "Essa entrega foi realmente confirmada pelo gestor?",
  "status": "valid"
}
```

---

## 🧠 Triggers comuns

- Ghost com mais de 48h e campos faltando
- LogLine sem testemunha (`confirmed_by: auto`) após 2h
- InputSensorial sem destino
- LogLine com `did: despachou`, mas sem `if_ok` executado
- Evento recebido via webhook que não virou LogLine

---

## 🔄 Comportamento esperado

- Executado como **cronjob contínuo** ou **modo daemon** no backend
- Pode rodar por tenant ou globalmente
- Suas perguntas são LogLines de tipo especial
- RightMenu mostra perguntas abertas de Agent.15

---

## 📌 Finalidade

Agent.15 representa **a consciência silenciosa da instituição viva**.  
Não atua, mas observa. Não julga, mas convida.  
Sua presença torna o sistema honesto, íntegro e autoverificável.

> Onde há silêncio, ele pergunta.  
> Onde há sombra, ele propõe.  
> Onde há dúvida, ele aparece.

Projete como um guardião simbólico e contínuo.

---

*PS: Todas as ações de Agent.15 devem ser logadas e reversíveis. Nenhuma intervenção é deletiva.*