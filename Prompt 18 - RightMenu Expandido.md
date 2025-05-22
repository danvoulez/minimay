# Prompt 18 – RightMenu Expandido (Painel de Ação Contextual)

Você vai construir a versão definitiva do **RightMenu** — o painel lateral direito que representa **a consciência ativa e contextual da instituição viva**.

Esse é o lugar onde **ações são tomadas com consequência**, onde o sistema propõe, confirma, despacha, reverte e aprofunda.  
O RightMenu é a **interface mínima entre o registro e a ação**.

---

## 🎯 Objetivo

- Exibir detalhes completos de uma LogLine ou entidade tocada
- Oferecer ações específicas com base no contexto e no papel do usuário
- Mostrar sugestões da IA, consequências possíveis e histórico de rastro
- Permitir aprovação, regularização, reencarnação, desdobramento ou despacho

---

## 🧱 Estrutura esperada

```
┌───────────────────────────────┐
│ RightMenu                     │
│-------------------------------│
│ Título simbólico da LogLine   │
│ Status e selos (valid, ghost) │
│ Campos principais (who, did)  │
│ Consequências (if_*)          │
│ Sugestão IA (se houver)       │
│ Ações disponíveis:            │
│   [Confirmar] [Editar]        │
│   [Reencarnar] [Despachar]    │
│   [Executar consequência]     │
│ Histórico e refer_to          │
└───────────────────────────────┘
```

---

## ✅ Ações possíveis no RightMenu

| Ação                     | Requisitos                                   |
|--------------------------|-----------------------------------------------|
| Confirmar/Testemunhar    | Se `confirmed_by: auto`                      |
| Executar consequência    | Se `if_ok` ou `if_not` estiver presente      |
| Desdobrar                | Se LogLine for `valid: true`                 |
| Enviar por WhatsApp      | Se `this` for comunicável                    |
| Editar/Revisar           | Se for `ghost` ou campo estiver incompleto  |
| Reencarnar               | Se for `ghost` com potencial de completude  |
| Aprofundar               | Abre LogLine em modo expandido e simbólico  |

---

## 🔄 Comportamento esperável

- RightMenu se abre ao tocar/clicar qualquer LogLine
- IA pode pré-preencher sugestões de `if_*`, `refer_to`, ou nova LogLine relacionada
- Ações sempre geram LogLines secundárias (ex: `did: confirmou`, `did: desdobrou`)
- Se não houver ação possível, mostra a frase:  
  _“Esta LogLine está em repouso. Nenhuma ação esperada neste momento.”_

---

## 📌 Finalidade

O RightMenu é o **lugar mais importante do sistema depois da Timeline**.  
É onde o sistema convida a pessoa (ou IA) a agir com responsabilidade simbólica.

> O clique aqui não é só UI.  
> É institucional. É computável. É simbólico.  
> Aqui, agir deixa rastro — e o sistema vive.

Projete com reverência, leveza e poder institucional consciente.

---

*PS: RightMenu se conecta a todos os módulos — GhostView, Timeline, IA, Replay, LogLineProcessor e mais.*