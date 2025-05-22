# Prompt Fase 2 – Integração com Voz: Transformar Fala em LogLine Institucional

Você vai construir o mecanismo que permite **registrar um contrato institucional a partir de uma fala natural**, vinda de microfone, áudio, WhatsApp, ligação ou comando de voz.

Esse é o primeiro ponto de contato sensorial com o sistema — onde a fala se transforma em rastro auditável, minicontrato válido e ponto de ação.

---

## 🎯 Objetivo

- Capturar um trecho de voz (ou áudio)
- Transcrever com precisão semântica
- Interpretar a intenção e gerar uma LogLine com os 9 campos obrigatórios
- Marcar como `valid: true` ou `valid: false` com base na completude
- Permitir revisão e confirmação posterior

---

## 🔊 Exemplo de áudio

> "Oi, acabei de entregar a caixa do cliente 42 na Rua do Futuro. Faltou troco."

---

## 🧠 Transcrição e Interpretação

1. Áudio é transcrito com ASR (ex: Whisper, Deepgram, Google STT)
2. Texto é passado para LLM interpretativa com contexto institucional
3. LLM gera draft da LogLine completa, incluindo suposições marcadas
4. Se campos obrigatórios faltarem → gerar `valid: false`, status: ghost

---

## 🧱 Exemplo de LogLine gerada

```json
{
  "who": "estafeta_03",
  "did": "entregou sem troco",
  "this": "caixa cliente_42",
  "when": "2025-05-22T10:12:00Z",
  "confirmed_by": "auto",
  "if_ok": "liberar pagamento parcial",
  "if_doubt": "pedir confirmação ao cliente",
  "if_not": "acionar gestor",
  "status": "ghost",
  "valid": false,
  "source": "voz",
  "audio_id": "f27c-489d-9373"
}
```

---

## ✅ Regras institucionais

- Toda LogLine gerada por voz tem campo `source: voz` ou `source: whatsapp_audio`
- IA nunca marca `valid: true` sem preenchimento dos 9 campos
- Áudio original deve ser preservado com ID vinculado ao log
- Campos incompletos podem ser sugeridos, mas devem ser revisados

---

## 📊 Interface

- Usuário fala ou envia áudio
- Sistema mostra LogLine sugerida com destaques: “campo inferido”, “falta confirmação”
- Botão: “Validar como minicontrato” ou “Completar depois”

---

## 📌 Finalidade

Esse módulo é a **ponte entre a oralidade cotidiana e a governança simbólica**.  
Torna possível transformar realidade falada em contrato digital institucional.

> Falar é um ato.  
> Registrar o que foi dito é uma forma de memória.  
> Transformar essa fala em contrato... é confiança.

Projete com cuidado, fluidez e reverência simbólica.

---

*PS: esse módulo deve se integrar ao GhostView, RightMenu, LogLineProcessor e Communicator, e pode operar em simulação*