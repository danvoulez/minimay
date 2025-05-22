# Prompt 6 – WhatsApp Institucional (Modo Completo Revisado)

Você vai construir o modo `Communicator` do sistema MINICONTRATOS com **estética de WhatsApp**,  
mas com **função de rastreamento institucional, IA viva e contratos embutidos**.

É uma conversa, mas também é um registro.  
É sensorial, mas também é auditável.  
É social, mas também é institucional.

---

## 🎯 Objetivo

- Criar um ambiente de troca natural, visualmente elegante
- Incluir a IA como participante viva, com proposta de LogLines
- Transformar mensagens em rastro — com ou sem intervenção
- Incorporar ações institucionais (confirmar, despachar, completar)

---

## 🧱 Estrutura

```
┌──────────────┬────────────────────────────┬──────────────┐
│ LeftMenu     │        ChatView            │ RightMenu    │
└──────────────┴────────────────────────────┴──────────────┘
```

### LeftMenu
- Lista de conversas (pessoa, grupo, IA)
- Filtro por tags (entregas, incidentes, turno)
- Atalhos para “IA viva”, “Favoritos”, “Prioridade”
- Indica chats com LogLines recentes

### ChatView (centro)
- Blocos de:
  - Texto simples (humanos)
  - Mensagens da IA (identificadas)
  - LogLines auditáveis (contrato expandido, selado)
- Campo inferior:
  ```
  > Digite ou descreva o que ocorreu...
  [______________________________] [Enviar]
  ```

### RightMenu
- Detalhes do LogLine destacado
- Ações rápidas:
  - Confirmar
  - Editar campos
  - Despachar para outro
  - Cancelar ou revisar
- Histórico da LogLine e de sua cadeia

---

## 🤖 Papel da IA

A IA está em **modo contínuo e responsivo**, atuando como:

- Cronista: resume o que está sendo discutido
- Propositora: transforma trechos em LogLines sugeridas
- Auditora: aponta inconsistências, faltas de testemunha
- Canal de ação: oferece despachos automáticos ou revisão humana

A IA nunca confirma ou publica sozinha, mas pode agir sob delegação.

---

## ✅ Rastro e Contratos

- Toda LogLine nasce com `status: ghost`
- Ao ser confirmada, vira `valid` e entra na timeline `/logline`
- Cada LogLine:
  - Pode ser citada em conversas
  - Pode ser expandida, despachada ou corrigida
  - É visível como bloco com moldura simbólica

---

## 🎨 Estilo

- WhatsApp institucional: sem emojis, sem gírias
- Paleta premium (silenciosa, noir, clara e escura)
- Transições suaves
- Feedbacks visuais de rastro: “registrado”, “aguardando testemunha”
- Blocos da IA com tipografia diferenciada
- RightMenu com estrutura de “cartório lateral”

---

## 📌 Finalidade

Essa não é uma cópia do WhatsApp.  
É a sua versão auditável, semântica e institucional.

> Aqui, conversa tem rastro.  
> Silêncio tem valor.  
> E cada fala pode virar contrato.

Construa com base nesses princípios, e com espaço para crescer.

---

*PS: essa tela deve ser integrada com LogLine ChatView e sincronizada com IA contínua por WebSocket.*