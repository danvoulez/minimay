# Prompt 21 – Webhook Receiver (Entrada de Eventos Externos)

Você vai criar o **Webhook Receiver** do sistema MINICONTRATOS.  
Esse módulo é o ponto de entrada para **sinais externos** (mensagens, formulários, sensores, APIs) que serão transformados em:

- LogLines completas (`valid: true`)
- Ghosts (`valid: false`)
- Ou entradas pendentes para interpretação da IA

---

## 🎯 Objetivo

- Receber dados de fora via chamadas HTTP POST
- Validar, interpretar e transformar em LogLine simbólica
- Rastrear origem, estrutura e intenção do sinal
- Acionar IA se necessário (`agent.14` ou `agent.15`)
- Permitir fallback institucional para dados ambíguos

---

## 🧱 Estrutura esperada

```
POST /api/webhook

Headers:
  Content-Type: application/json
  X-Source: whatsapp | form | sensor | api | camera

Body:
{
  "external_id": "abc123",
  "source": "whatsapp",
  "payload": { ... },
  "received_at": "2025-05-21T10:15:00Z"
}
```

---

## 🔄 Processamento esperado

1. **Verificar tipo de origem (`source`)**
2. **Tentar criar LogLine com base em regras institucionais**
3. Se incompleto ou ambíguo:
   - Criar Ghost LogLine
   - Acionar Agent.15 com `did: questionou_validez`
4. Gerar log de entrada:

```json
{
  "who": "webhook.system",
  "did": "recebeu_webhook",
  "this": "external.whatsapp.msg_123",
  "status": "valid"
}
```

---

## ✅ Exemplo de LogLine gerada a partir do WhatsApp

```json
{
  "who": "cliente_rafael",
  "did": "solicitou_entrega",
  "this": "caixa 002",
  "when": "2025-05-21T10:15:00Z",
  "confirmed_by": "agent.14",
  "status": "valid",
  "origin": "whatsapp"
}
```

---

## 📌 Finalidade

Esse receiver transforma o sistema em um **organismo sensorial**.  
Tudo que chega de fora é recebido com rastreabilidade, dúvida simbólica e intenção de virar contrato.

> Onde há gesto, pode haver intenção.  
> Onde há dado, pode haver contrato.  
> Onde há entrada, pode haver rastro.

Projete com robustez, logging e capacidade de fallback semântico.

---

*PS: esse receiver deve ser compatível com múltiplas fontes e pode ser usado em testes via `curl`, Postman ou integração institucional.*