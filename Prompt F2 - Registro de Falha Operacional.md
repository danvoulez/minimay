# Prompt Fase 2 – Registro de Falha Operacional como LogLine

Você vai criar o mecanismo para **registrar qualquer tipo de falha percebida no sistema como um ato institucional**, usando a estrutura da LogLine.

Esse é o canal simbólico onde operadores, IAs ou sistemas podem declarar erros — sem medo, com rastro e consequência possível.

---

## 🎯 Objetivo

- Transformar falhas (de sistema, humanas, de contexto ou de entrega) em LogLines
- Atribuir autor (quem registrou), testemunha (quem viu), e consequências
- Usar estrutura institucional da LogLine para criar histórico confiável de erros
- Permitir tratamento automatizado, sugestão de solução e revisão

---

## 🧱 Exemplo de LogLine de falha

```json
{
  "who": "estafeta_04",
  "did": "relatou falha",
  "this": "cliente ausente na entrega 078",
  "when": "2025-05-22T11:55:00Z",
  "confirmed_by": "gestor_fabio",
  "if_ok": "reagendar",
  "if_doubt": "pedir geolocalização",
  "if_not": "encerrar turno",
  "status": "valid",
  "type": "falha_operacional",
  "severity": "moderada"
}
```

---

## ✅ Campos adicionais esperados

| Campo       | Descrição                                |
|-------------|--------------------------------------------|
| `type`      | `"falha_operacional"`, `"erro_sistema"`, `"atraso"`, `"interrupcao"` |
| `severity`  | `"leve"`, `"moderada"`, `"grave"`, `"crítica"` |
| `impact`    | Opcional – texto ou enum sobre a área afetada |
| `auto_filed`| Se foi aberto por IA ou módulo interno (true/false) |

---

## 📊 Interface

- Botão visível: “Registrar falha”
- Campos visuais rápidos: tipo da falha, turno/caixa envolvida, causa aparente
- IA sugere consequências possíveis (`if_*`) com base em histórico
- Registro pode ser feito via `/logline`, `/communicator`, ou `/ghost`

---

## 🧠 Integrações

- Falhas alimentam o cronjob de regularização
- Podem gerar Ghosts se incompletas
- São analisadas por LLM (`ghost_revisor`) para gerar perguntas ou recomendações
- IA pode cruzar falhas com `did: validou_entrega`, `did: cancelou_venda`, etc.

---

## 📌 Finalidade

Esse módulo cria um canal seguro, digno e rastreável para falhar.  
Faz com que o erro deixe de ser ruído — e passe a ser **rastro, dado e aprendizado institucional**.

> Toda falha é uma pergunta: o que deveria ter acontecido?  
> Registrar o erro é o primeiro passo para governar o caos.

Projete com clareza, suavidade e consequência computável.

---

*PS: toda falha registrada entra no GhostView se `valid: false` e pode ser reaparecida via cronjob se não resolvida*