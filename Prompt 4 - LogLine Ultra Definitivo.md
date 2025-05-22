# Prompt 4 – Tela `/logline` Ultra Definitiva: ChatGPT Institucional com Consequência, Navegação e Ação

Você é responsável por construir a tela principal do sistema MINICONTRATOS: `/logline`.

Essa tela é o **clone institucional do ChatGPT**, conectado ao banco semântico da organização (LogLine).  
Ela deve reunir: entrada fluida, renderização visual deslumbrante, navegação por instâncias e ações contextuais sobre registros.

---

## 🧩 Estrutura Geral da Interface

```
┌────────────────┬────────────────────────────┬───────────────┐
│  Painel Esquerdo │        Tela Central        │ Painel Direito │
└────────────────┴────────────────────────────┴───────────────┘
```

---

## 1. 🧭 Painel Esquerdo (`LeftMenu`) — Navegação Institucional

### Função:
- Navegar entre instâncias de conversa, histórico de registros e visão pessoal/institucional

### Contém:
- [ + Novo Chat ] — cria nova instância de diálogo
- [ Minhas conversas ]
- [ Minicontratos ativos ]
- [ Timeline institucional ]
- [ Favoritos ]
- [ Settings (tema, IA, idioma) ]

### Estilo:
- Ícones táteis
- Transições suaves
- Sempre visível, sem ocupar o foco central

---

## 2. 💬 Tela Central — Chat com IA + Timeline Semântica

### Função:
- Entrada e visualização viva da operação institucional

### Contém:
- Campo de entrada (estilo ChatGPT):
  ```
  > o que aconteceu?
  [__________________________________________] [Enviar]
  ```

- Renderização de mensagens:
  - Do usuário
  - Da IA (quem: `IA`)
  - De LogLines vivas (`status: ghost`, `valid`, etc)
  - De cards, tabelas, insights, comandos, histórico

- Suporte a:
  - Renderizador visual de LogLine
  - Sugestões de fluxo
  - Auto-complete institucional

---

## 3. ⚙️ Painel Direito (`RightMenu`) — Ação Contextual

### Função:
- Mostrar detalhes e permitir ações sobre qualquer LogLine selecionada

### Contém:
- Detalhes do LogLine expandido
- Campos editáveis
- Status completo (`ghost`, `confirmed_by`, `if_ok`, etc)
- Ações:
  - Confirmar
  - Completar campos
  - Despachar
  - Histórico do contrato
- Sugestões de consequência
- Botão: “Ver em modo completo”

### Estilo:
- Camada que desliza com gesto ou clique
- Transparente, leve, auditável

---

## 🤖 Comportamento da IA

- Toda entrada é processada por `processMessage(text, user_id)`
- A IA pode:
  - Criar LogLines
  - Completar registros
  - Despachar eventos
  - Oferecer insights, análises e resumo
- Cada resposta da IA é registrada como LogLine com `who: IA`

---

## ✅ Regras Institucionais

- Toda interação gera ou complementa LogLine
- Nenhum dado é apagado
- O operador pode revisar qualquer passo
- `ghosts` aparecem com selo e são dignos
- Toda ação é auditável com `did`, `who`, `when`, `confirmed_by`

---

## 🎨 Estilo

- Mosaic Engine para tema e variáveis visuais
- Transições suaves
- Cartões com brilho institucional
- Nenhum elemento genérico ou despersonalizado

---

## 🧠 Finalidade

Essa é a tela onde a IA pensa, fala e age.  
É onde o operador escreve a história institucional por meio de linguagem.

> Tudo que for dito aqui pode virar contrato.  
> E tudo que for contrato pode ser completado, confirmado, encaminhado — com consequência.

Essa é a tela viva da instituição.  
Projete com essa responsabilidade.

---

*PS: continuação aberta para extensões como multi-chats, busca semântica, insights visuais e auto-orquestração institucional.*