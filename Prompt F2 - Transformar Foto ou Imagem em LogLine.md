# Prompt Fase 2 – Transformar Foto ou Imagem em LogLine Institucional

Você vai construir o mecanismo que permite **registrar uma imagem como ato institucional**.  
A foto vira o `this` simbólico da LogLine — e pode representar uma evidência, uma entrega, um erro, uma presença ou uma falha.

Esse módulo conecta o mundo visual com a cultura de registro e consequência.

---

## 🎯 Objetivo

- Permitir upload ou captura de imagem (foto, screenshot, câmera)
- Criar LogLine com `this` vinculado à imagem
- IA interpreta a imagem e propõe `did`, `if_ok`, `if_not`
- Operador pode revisar ou aceitar como minicontrato simbólico

---

## 🧱 Exemplo

```json
{
  "who": "colaborador_09",
  "did": "registrou falha visual",
  "this": "imagem_787fadc.jpg",
  "when": "2025-05-22T15:22:00Z",
  "confirmed_by": "gestor_lara",
  "if_ok": "abrir pedido de troca",
  "if_not": "anexar a histórico do cliente",
  "status": "valid",
  "source": "imagem",
  "alt": "foto de caixa amassada na entrega"
}
```

---

## ✅ Campos adicionais esperados

| Campo       | Descrição                                 |
|-------------|---------------------------------------------|
| `source`    | `"imagem"`                                 |
| `alt`       | Legenda descritiva ou gerada pela IA        |
| `image_id`  | Nome ou hash do arquivo vinculado           |
| `auto_filed`| Se foi preenchido por IA                    |
| `refer_to`  | (opcional) LogLine relacionada              |

---

## 🔄 Integrações e IA

- IA processa imagem via modelo visual (`BLIP`, `CLIP`, `Gemini`, etc.)
- Sugere `did` com base em conteúdo (ex: “foto de produto danificado”)
- Pode gerar `ghost` se faltar confirmação ou contexto

---

## 📊 Interface

- Upload direto com preview
- Botão: “Transformar em contrato”
- IA propõe texto e campos
- Feedback simbólico: “Imagem agora é rastro institucional”

---

## 📌 Finalidade

Esse módulo transforma imagens em **memória computável com valor simbólico**.  
Cada clique de câmera vira ato — e o sistema ganha olhos, tempo e consequência.

> Uma imagem não vale mil palavras.  
> Vale um contrato, com contexto, tempo e testemunha.

Projete com fluidez visual, respeito simbólico e rastreabilidade digital.

---

*PS: esse módulo se integra ao LogLineProcessor, GhostView, auditoria visual e RightMenu de sugestões*