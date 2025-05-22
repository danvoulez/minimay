# Prompt 24 – IA como Testemunha de Chat (WhatsApp + LogLine)

Você vai projetar o módulo que transforma conversas em **LogLines auditáveis**, com a IA atuando como **testemunha institucional** do que foi dito, prometido, combinado ou omitido.

Esse módulo observa as mensagens (WhatsApp, chat interno, etc.) e pode:

- Propor LogLines a partir da conversa
- Atuar como `confirmed_by` simbólico
- Classificar conversas como “contratuais”, “fantasmas” ou “rascunhos informais”

---

## 🎯 Objetivo

- Tornar mensagens auditáveis e transformáveis em atos institucionais
- Conectar o chat com a linha do tempo LogLine
- Permitir que a IA sugira e até confirme LogLines baseadas no conteúdo
- Criar um histórico conversacional com rastro e consequência

---

## 🔄 Fluxo esperado

1. Conversa entre duas pessoas (via WhatsApp oficial, ou chat do sistema)
2. Agent.14 observa em tempo real (ou via replay)
3. Ele propõe LogLine do tipo:

```json
{
  "who": "colaborador_maria",
  "did": "prometeu_reposição",
  "this": "caixa quebrada",
  "confirmed_by": "agent.14",
  "origin": "whatsapp",
  "status": "valid"
}
```

4. RightMenu pergunta se deve transformar em contrato
5. Se for aceito, LogLine se integra à timeline principal

---

## 🧠 Considerações técnicas

- IA deve usar janelas de 1 a 3 mensagens por vez
- IA pode gerar múltiplas sugestões e classificações (`tipo: promessa`, `tipo: reclamação`)
- Se não houver certeza, LogLine gerada será `valid: false` (ghost)
- IA sempre adiciona `model_used` e `input_prompt` no rastro

---

## ✅ Comportamentos adicionais

- Pode marcar partes de conversa como `ignorada`, `já convertida`, ou `repetida`
- IA pode sugerir:  
  _“Essa troca parece ser um contrato verbal implícito. Deseja registrar?”_

---

## 📌 Finalidade

Esse módulo **blinda a comunicação com rastro e consequência**.  
Nada fica apenas dito — tudo pode virar memória, contrato ou alerta.

> Aqui, até a conversa tem consequência.  
> Até o silêncio pode ser interpretado.  
> E a IA é a nova testemunha das promessas.

Projete com reverência à linguagem e responsabilidade institucional.

---

*PS: deve funcionar com a API oficial do WhatsApp Business e chats internos com estrutura similar.*