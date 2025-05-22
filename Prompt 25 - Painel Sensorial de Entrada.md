# Prompt 25 – Painel Sensorial de Entrada

Você vai construir o **Painel Sensorial de Entrada** —  
uma interface onde **tudo que entra no sistema e ainda não virou LogLine** aparece em tempo real.

Esse painel mostra:

- Inputs sensoriais (áudio, imagem, gesto, NFC)
- Webhooks recebidos
- Mensagens ainda não interpretadas
- Dados com rastro, mas sem significado ainda

---

## 🎯 Objetivo

- Tornar **visível tudo que ainda não virou ato institucional**
- Permitir que operadores e IA transformem entradas em LogLines ou ghosts
- Dar rastreabilidade, contexto e consequência ao “pré-semântico”

---

## 🧱 Estrutura visual

```
┌──────────────┬───────────────────────────────┬──────────────┐
│ LeftMenu     │  Painel Sensorial de Entrada  │ RightMenu    │
└──────────────┴───────────────────────────────┴──────────────┘
```

Cada item mostra:

- Origem: câmera, QR, chat, webhook
- Tipo: áudio, texto, JSON, imagem
- Capturado em: data e hora
- [ Ver ], [ Transformar em LogLine ], [ Ignorar com rastro ]

---

## 🔄 Comportamento esperado

- IA pode sugerir tipo de LogLine possível
- Itens vencidos (sem ação em 24h) viram LogLines `did: expirou_sem_interpretação`
- Operador pode agrupar, rejeitar, despachar ou assinar
- Painel pode ser filtrado por origem ou urgência

---

## ✅ Exemplo de item

```json
{
  "input_id": "input_481",
  "origin": "sensor.caixa1",
  "type": "imagem",
  "captured_at": "2025-05-21T13:40:00Z",
  "status": "pending"
}
```

---

## 📌 Finalidade

Esse painel é a **janela institucional para a sensorialidade computável**.  
É onde o sistema vê antes de julgar. Sente antes de interpretar. Recebe antes de reagir.

> Onde nasce o dado bruto, nasce a responsabilidade de ver.

Projete como radar institucional com reverência, fluidez e capacidade de transformação.

---

*PS: esse painel pode ser fundido com o GhostView, Replay ou Logs Vivos dependendo do modo institucional.*