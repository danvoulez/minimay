# Prompt 5 – Tela `/communicator`: Chat Institucional com IA e Consequência (Revisado)

Você é responsável por construir o modo `Communicator` do sistema MINICONTRATOS —  
um ambiente de mensagens internas onde colaboradores e IA interagem em tempo real, com rastro.

Esse modo **não é um chat comum**.  
É uma conversa viva, **semântica, auditável, conectada à LogLine**.

---

## 🎯 Objetivo

- Permitir conversas entre pessoas com registro institucional
- Ter uma IA assistente que participa, sugere e registra
- Criar ou derivar LogLines a partir de trocas naturais
- Trazer visual e experiência parecidos com um WhatsApp premium, mas com rastro e consequência

---

## 🧱 Estrutura da tela

```
┌──────────────┬──────────────────────────┬──────────────┐
│ LeftMenu     │   Conversa institucional │ RightMenu    │
└──────────────┴──────────────────────────┴──────────────┘
```

### 1. LeftMenu
- Lista de chats (pessoa, grupo, IA, tags institucionais)
- Nova conversa
- Acesso rápido ao chat com IA
- Marcação de não lido, prioridade ou tags semânticas

### 2. Centro (ChatView)
- Blocos de mensagens:
  - Texto entre humanos
  - Blocos da IA (sugestivos, estruturados, com ação)
  - Blocos de LogLine geradas ou citadas
- Input inferior fixo:
  ```
  > Escreva algo...
  [_____________________________] [Enviar]
  ```
- Suporte futuro a voz, imagens e comandos por botão

### 3. RightMenu
- Detalhes do registro gerado ou citado
- Ações: confirmar, completar, despachar
- Mini timeline daquela LogLine
- Campos para `if_ok`, `if_not`, `confirmed_by`
- Visualização rápida de pendências

---

## 🤖 Comportamento da IA

- Sempre presente e contextual
- Atua como:
  - Testemunha
  - Auditora
  - Propositora de LogLine
  - Canal de criação assistida

Exemplo:

> [Humano] “A máquina travou de novo”
>
> [IA] “Deseja registrar como incidente técnico?”
>
> [Humano] “Sim, só não quero culpar ninguém”
>
> [IA] “Registrado como ghost. Deseja despachar para equipe de manutenção?”

---

## ✅ Regras de rastreio

- Toda LogLine gerada aparece no chat, na `/logline`, e pode ser revista
- Nenhuma sugestão da IA é aplicada sem ação clara do humano
- IA pode gerar rascunhos (`ghost`) proativamente, mas sem marcar como valid

---

## 🎨 Estética

- Interface mobile-first
- Blocos suaves, premium, institucionais
- IA com cor e ícone distintos
- LogLines com moldura simbólica
- Transições leves, sem scroll brusco
- Feedback visual claro de "registrado", "rascunho salvo", "despachado"

---

## 🧠 Finalidade

Esse modo `Communicator` substitui mensagens frágeis por **diálogos com memória e consequência**.

> Toda conversa pode virar ação.  
> Toda palavra pode virar contrato.  
> A IA está aqui para lembrar, não para mandar.

Construa esse modo como se fosse o novo caderno preto da operação.