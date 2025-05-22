# Prompt 3 – Tela `New` Sensorial (Revisado)

Você é responsável por criar a tela `New` do sistema MINICONTRATOS —  
uma interface sensorial, rápida e institucional para registrar acontecimentos reais em forma de LogLines.

Essa tela não é um formulário comum.  
Ela é um **ambiente tátil onde cada clique vira contrato.**

---

## 🎯 Objetivo

- Permitir que qualquer pessoa **registre um acontecimento com 3 a 5 toques**
- Apresentar **uma pergunta por vez**, com sugestões personalizadas
- Tratar qualquer entrada como legítima, mesmo incompleta
- Gerar LogLines auditáveis com status `valid` ou `ghost`
- Incentivar a cultura do registro com leveza, não com cobrança

---

## 🧭 Integração visual com o sistema

Essa tela é o **modo `/new`** da estrutura principal:

```
┌──────────────┬───────────────────────┬─────────────┐
│ LeftMenu     │   Tela de Registro    │ RightMenu   │
└──────────────┴───────────────────────┴─────────────┘
```

- O **LeftMenu** continua disponível para voltar ao histórico ou iniciar um novo
- O **RightMenu** pode:
  - Mostrar sugestões do LLM
  - Completar consequências (if_ok, if_not, etc)
  - Despachar a LogLine em tempo real
  - Sugerir quem pode ser testemunha

---

## 🧱 Etapas da tela

### Etapa 1: Quem fez isso?
```
[ Eu mesmo ]     [ Outra pessoa ]
```
→ Clique colapsa a pergunta e avança

### Etapa 2: O que foi feito?
Frases sugeridas com base no histórico:
```
[ Confirmei entrega ]
[ Cliente reclamou ]
[ Abri loja com atraso ]
```

### Etapa 3: Sobre o quê?
```
[ Caixa 00321 ]
[ Cliente João ]
[ Outro... ]
```

### Etapa 4: Consequências (opcional)
```
[ if_ok: avisar gestor ]
[ if_not: marcar incidente ]
[ if_doubt: IA analisa depois ]
```
ou
```
[ Deixar para decidir depois ] → insere `auto`
```

---

## ✅ Registro final

- Exibe resumo da LogLine antes de registrar
- Permite:
  - [ Registrar ]
  - [ Despachar para alguém ]
  - [ Completar agora com IA ]
- O registro **aparece imediatamente na `/logline`**, como item `valid` ou `ghost`

---

## 🤖 IA assistente

- Sugere frases com base em `user_id` + histórico
- Sugere consequências plausíveis
- Pode preencher ou sugerir `confirmed_by`

---

## 🎨 Estética

- Estilo de fala, não de formulário
- Cada passo parece natural, quase como conversar
- Animação de colapso de pergunta ao responder
- Feedback tátil: “registro criado”, “rascunho salvo”, “despachado”

---

## 🧠 Finalidade

Essa tela **ensina a cultura do registro sem punir**.  
É onde o gesto vira consequência.  
Onde o silêncio pode ser registrado com dignidade.

> O contrato nasce aqui.  
> Mesmo incompleto, ele já tem valor.  
> O sistema ajuda, mas nunca julga.

Construa essa tela como se fosse a primeira fala da instituição com o operador.