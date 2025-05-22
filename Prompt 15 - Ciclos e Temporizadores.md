# Prompt 15 – Ciclos e Temporizadores: Revalidação, Auditoria e Despertar de Pendências

Você vai construir o **sistema institucional de temporização, reaparição e verificação de registros**  
no ecossistema MINICONTRATOS.

Esse módulo mantém a plataforma viva, coerente e em constante verificação — despertando pendências, revisando fantasmas e reativando ciclos abertos.

---

## 🎯 Objetivo

- Detectar LogLines incompletas, pendentes ou sensíveis ao tempo
- Reativar registros que precisam de nova atenção
- Agendar revisões, auditorias ou encerramentos automáticos
- Tornar o tempo um agente institucional legítimo

---

## ⏱️ Tipos de Ciclos

### 1. **Revalidação Programada**
- Verifica LogLines com `valid: false` há mais de X dias
- Se contexto mudou, IA tenta completar ou arquivar

### 2. **Ciclos Incompletos**
- Detecta registros com `if_ok`, `if_doubt`, `if_not` mas sem execução
- Relembra o autor ou sugere ação no RightMenu

### 3. **Auditorias Semestrais**
- Gera LogLines tipo `did: iniciou_auditoria_institucional`
- IA revisa % dos contratos antigos para detectar omissões

### 4. **Despertar de Ghosts Dormidos**
- Ghosts inativos há mais de N dias voltam à GhostView com selo “ignorado”
- IA pergunta: “Esse registro ainda importa?”

---

## 🧱 Exemplo de LogLine gerada pelo temporizador

```json
{
  "who": "system.cron.supervisor",
  "did": "reativou_ghost",
  "this": "registro turno 42",
  "when": "2025-05-22T00:00:00Z",
  "status": "valid",
  "confirmed_by": "auto",
  "reason": "ghost dormido há 20 dias sem resposta"
}
```

---

## 🔁 Lógica de execução

- Roda diariamente às 00:00
- Busca registros por critérios:
  - `status: ghost`
  - `created_at < today - X dias`
  - `if_*` presente mas sem LogLine de execução
- Avalia contexto com IA
- Gera ações simbólicas com LogLine

---

## ✅ Resultados esperados

- IA pode:
  - completar com nova sugestão
  - notificar autor original
  - despachar para nova testemunha
  - marcar como encerrado por tempo (com `confirmed_by: timeout.policy`)

---

## 📌 Finalidade

Esse módulo dá à plataforma **senso de tempo, memória e vigilância simbólica**.  
O sistema não esquece. Ele **retorna ao que foi deixado em aberto**, e pergunta: “Ainda é verdade?”

> O tempo institucional não é cronômetro: é consequência adormecida.  
> O sistema acorda o que esquecemos — com dignidade e rastreio.

Projete com regularidade, compaixão operativa e firmeza simbólica.

---

*PS: esse módulo deve gerar logs visíveis, integrados à GhostView e RightMenu, e funcionar em simulação quando o sistema estiver em modo de teste*