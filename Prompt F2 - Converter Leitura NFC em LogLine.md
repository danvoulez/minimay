# Prompt Fase 2 – Converter Leitura NFC em LogLine Institucional

Você vai criar o mecanismo que permite **converter uma leitura NFC (etiqueta, cartão, pulseira)**  
em uma LogLine institucional válida, rastreável e carregada de consequência.

Esse módulo transforma gestos físicos em **contratos digitais simbólicos** — com rastro, tempo, autor e ação definida.

---

## 🎯 Objetivo

- Capturar uma leitura NFC (via celular ou leitor)
- Traduzir o ID lido em uma entidade do sistema (`pessoa`, `objeto`, `entrega`, `caixa`)
- Gerar uma LogLine com base no contexto + histórico do item lido
- Permitir que IA preencha campos faltantes e sugira consequência

---

## 🧱 Exemplo

### Leitura NFC:

- Tag ID: `NFC-91A4C3D2`
- Reconhecida como: `caixa_012`, entrega do pedido `ven_874`

### LogLine gerada:

```json
{
  "who": "estafeta_07",
  "did": "registrou entrega via nfc",
  "this": "caixa_012",
  "when": "2025-05-22T13:45:00Z",
  "confirmed_by": "auto",
  "if_ok": "liberar pagamento",
  "if_not": "acionar cliente",
  "status": "valid",
  "source": "nfc",
  "nfc_id": "NFC-91A4C3D2"
}
```

---

## ✅ Campos adicionais esperados

| Campo       | Descrição                                |
|-------------|--------------------------------------------|
| `source`    | Sempre `"nfc"`                             |
| `nfc_id`    | ID lido da tag                             |
| `matched_to`| Objeto reconhecido (`entrega_874`, `caixa_01`) |
| `auto_filed`| `true` se a IA completou parte dos campos   |

---

## 🔄 Integrações e Comportamento

- IA verifica histórico do `this` (última entrega, status, confirmação)
- Campos ausentes podem ser inferidos ou marcados como `ghost`
- Pode disparar fluxo de confirmação no RightMenu (ex: “confirme recebimento da caixa_012”)
- Registro visível em `/logline`, com selo: “via leitura NFC”

---

## 📊 Interface

- Ao detectar leitura NFC válida:
  - Mostra prévia da LogLine gerada
  - Permite completar ou confirmar
  - Destaca se registro for incompleto

---

## 📌 Finalidade

Esse módulo transforma objetos em **entidades semânticas do sistema**,  
e cada toque físico em **um contrato simbólico com rastro e consequência**.

> Uma leitura NFC pode ser um simples clique…  
> ou o início de um ciclo institucional com rastreabilidade e memória.

Projete com fluidez, auditabilidade e gesto computável.

---

*PS: esse módulo deve conversar com LogLineProcessor, cronjob, RightMenu e fallback de ações incompletas*