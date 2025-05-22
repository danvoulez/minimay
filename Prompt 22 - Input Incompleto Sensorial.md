# Prompt 22 – Input Incompleto Sensorial (Pré-LogLine)

Você vai criar o sistema de **entrada sensorial bruta** do MINICONTRATOS —  
um repositório vivo de interações que ainda **não são LogLines**, mas carregam potencial institucional.

Esses inputs podem vir de toques, gestos, áudios, vídeos, imagens, escaneamentos ou sinais abstratos.  
São sementes de LogLines, ainda sem forma, aguardando sentido, testemunha ou desdobramento.

---

## 🎯 Objetivo

- Capturar sinais que ainda não têm `did`, `status` ou `who` definidos
- Armazenar como `InputSensorial` com hash, origem, horário e tipo
- Permitir que IA interprete, complete ou descarte
- Marcar se input virou LogLine (via `refer_to`)
- Ser auditável, reversível e institucional

---

## 🧱 Exemplo de estrutura de entrada

```json
{
  "input_id": "input_82398",
  "origin": "camera_entrada",
  "type": "imagem",
  "captured_at": "2025-05-21T13:48:00Z",
  "status": "pending",
  "refer_to": null
}
```

---

## 🔄 Interações esperadas

- IA (`agent.14`) pode rotular ou sugerir LogLine:
  - `did: pessoa_entrou`, `this: colaborador_joao`
- RightMenu pode mostrar preview do input
- Operador pode confirmar ou ignorar
- Ghosts podem nascer a partir desses inputs

---

## 🧠 Integrações

- Pode ser alimentado por:
  - Webhook externo
  - Upload manual de operador
  - Escaneamento NFC
  - Visão computacional
  - Microfone ambiente

- IA pode sugerir:  
  _"Esse gesto parece um pedido de turno."_  
  _"Esse áudio é um relato não estruturado."_  
  _"Essa imagem mostra um QR lido por colaborador."_  

---

## 📌 Finalidade

Esse módulo reconhece que **nem todo registro nasce completo**.  
Muitos atos legítimos surgem do gesto, da sombra, do som, do impulso.

> Aqui nasce o que ainda não tem nome.  
> O que não virou contrato, mas quer ser.  
> A pré-semântica da instituição vive aqui.

Projete como buffer institucional reversível e respeitoso.

---

*PS: inputs não utilizados devem expirar com rastro. Nada é perdido. Tudo é memória potencial.*