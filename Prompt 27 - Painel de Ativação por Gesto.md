# Prompt 27 – Painel de Ativação por Gesto

Você vai criar o **Painel de Ativação por Gesto** —  
uma interface e infraestrutura que permite que **interações táteis, cliques e aproximações** sejam interpretadas como **intenção institucional**.

Esse painel não exige digitação, nem escrita.  
Ele interpreta **toques, swipes, aproximações NFC, gestos com câmera, ou padrões de clique** como tentativas de criar LogLines.

---

## 🎯 Objetivo

- Capturar e interpretar gestos como intenção
- Conectar eventos físicos a LogTemplates institucionais
- Exibir feedback sensorial e simbólico (“ação registrada”, “cadastro iniciado”)
- Permitir operação completa por gestos, sem escrita

---

## 🧱 Exemplo de Gesto → LogLine

```json
{
  "who": "visitante_anonimo",
  "did": "acionou_gesto",
  "this": "painel_turno",
  "when": "2025-05-21T14:44:00Z",
  "status": "ghost",
  "confirmed_by": "auto"
}
```

- O campo `did` pode ser interpretado com auxílio da IA:  
  _“Esse gesto significa 'pedido de entrada em turno'?”_

---

## 🔄 Funcionalidades esperadas

- Painel mostra área sensível a gestos
- Pode ser ativado por:
  - clique em áreas silenciosas
  - aproximação de tag NFC
  - movimento captado por câmera (modo experimental)
  - toque sequencial em layout

- IA sugere qual LogTemplate aplicar
- Se validado, LogLine entra no sistema
- Se ambíguo, vira `input_sensorial` com marcação

---

## 🎨 Estética

- Deve parecer um painel institucional silencioso
- Ícones vivos, áreas de toque grandes, resposta tátil (som, cor, vibração)
- Inspirado na interação com terminais de acesso premium (aeroportos, Apple Store)

---

## 📌 Finalidade

Esse painel reconhece que **nem toda ação precisa ser verbalizada**.  
O toque é uma linguagem. O gesto é uma intenção. E a intenção tem rastro.

> Aqui, um gesto vira contrato.  
> Um toque vira dado.  
> E o sistema sente antes de ouvir.

Projete com foco em acessibilidade, fluidez e inteligência institucional.

---

*PS: esse painel é ideal para dispositivos de entrada rápida (tablets, quiosques, caixas de entrada simbólica).*