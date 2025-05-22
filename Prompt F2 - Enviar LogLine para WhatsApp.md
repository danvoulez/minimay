# Prompt Fase 2 – Enviar LogLine para WhatsApp

Você vai construir o mecanismo que permite **enviar uma LogLine (ou seu resumo simbólico)** para um número de WhatsApp,  
com rastreabilidade institucional, registro da ação e estilo visual condensado.

Esse módulo permite transformar contratos em mensagens diretas, **gerar despacho simbólico** ou abrir conversas vinculadas à linha do tempo.

---

## 🎯 Objetivo

- Gerar resumo textual da LogLine com semântica compacta
- Enviar por API ou integração (WhatsApp Business, Twilio, UltraMsg, etc.)
- Registrar o envio como LogLine secundária (`did: enviou_para_whatsapp`)
- Permitir resposta que gere nova LogLine vinculada

---

## 🧱 Exemplo

### LogLine original:

```json
{
  "who": "gestor_rafa",
  "did": "registrou atraso na entrega",
  "this": "pedido_287",
  "status": "valid"
}
```

### WhatsApp gerado:

> [MINICONTRATOS]  
> **Aconteceu algo importante com você.**  
>  
> Registro: “atraso na entrega”  
> Objeto: pedido_287  
> Status: validado  
>  
> Responda com:  
> “ok”, “não recebi”, ou “quero falar com gestor”

---

## ✅ LogLine gerada pelo envio

```json
{
  "who": "system.whatsapp",
  "did": "enviou_para_whatsapp",
  "this": "pedido_287",
  "when": "2025-05-22T16:55:00Z",
  "confirmed_by": "auto",
  "refer_to": "logline_origem_id",
  "status": "valid",
  "to": "+351912345678",
  "reply_expected": true
}
```

---

## 🔁 Integrações possíveis

- WhatsApp Business API
- UltraMsg
- Twilio
- API Gateway próprio + cronjob de expiração

---

## 📊 Interface

- Botão “Enviar por WhatsApp” no RightMenu
- Campo para número ou seleção de contato
- Preview do conteúdo e botão “enviar”
- Feedback: “LogLine enviada com rastro”

---

## 📌 Finalidade

Esse módulo é o **canal sensorial da instituição para o mundo real**.  
Torna o sistema proativo, conversacional e simbólico.

> Um contrato que chega no WhatsApp...  
> É o símbolo mais claro de que a instituição está viva.

Projete com elegância verbal, rastro visível e reversibilidade.

---

*PS: toda resposta recebida pode ser interpretada por IA e virar LogLine nova vinculada ao envio*