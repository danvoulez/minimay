# Prompt 11 – LogLineProcessor: Executor Institucional de Consequências

Você vai construir o **LogLineProcessor**: o mecanismo responsável por **executar as consequências descritas em uma LogLine**.

Esse módulo é o **órgão institucional da vontade registrada**. Ele interpreta os campos `if_ok`, `if_doubt` e `if_not` e transforma essas intenções em **ações concretas**, rastreáveis e auditáveis.

---

## 🎯 Objetivo

- Ler LogLines com `status: valid`
- Interpretar os campos de consequência (`if_ok`, `if_doubt`, `if_not`)
- Executar as ações correspondentes (diretamente ou por delegação)
- Registrar cada execução com uma nova LogLine
- Tratar erros e fallback com rastreabilidade

---

## 🧱 Exemplo de LogLine processável

```json
{
  "who": "estafeta_03",
  "did": "confirmou entrega",
  "this": "caixa_001",
  "when": "2025-05-21T14:22:00Z",
  "confirmed_by": "gestor_rafa",
  "if_ok": "liberar_pagamento",
  "if_doubt": "notificar_suporte",
  "if_not": "bloquear_cliente",
  "status": "valid"
}
```

---

## 🧠 Lógica do Processador

1. **Identifica LogLines `valid` com campos `if_*` não processados**
2. **Verifica contexto atual da operação** (permissões, estado do sistema, pendências)
3. **Executa a consequência apropriada** com base na validação ou resultado da LogLine:
   - Se `status: valid` → `execute(if_ok)`
   - Se `status: doubt` → `execute(if_doubt)`
   - Se `status: not_validated` ou falha → `execute(if_not)`
4. **Cria nova LogLine com rastro da execução**

---

## ✅ Formatos de consequência esperados

- `"liberar_pagamento"` → chama função financeira
- `"abrir_incidente"` → cria nova LogLine tipo `did: abriu incidente`
- `"notificar_suporte"` → envia mensagem via Communicator
- `"despachar_para_ia"` → invoca agente semântico

---

## 🧾 Registro da execução

Cada consequência executada deve gerar uma nova LogLine, como:

```json
{
  "who": "LogLineProcessor",
  "did": "executou_consequencia",
  "this": "liberar_pagamento",
  "when": "2025-05-21T14:23:00Z",
  "confirmed_by": "auto",
  "status": "valid",
  "refer_to": "logline_841"
}
```

---

## 🔄 Fallback e Erros

- Se a ação falhar, registrar nova LogLine `did: falha_na_execucao`
- IA pode tentar alternativa, gerar sugestão ou delegar
- Todas as tentativas e reações devem ter rastro

---

## 🔐 Permissões e Restrições

- Processador só age sobre LogLines `valid: true`
- Se for `"simulation: true"`, **executa no modo reversível**, sem efeitos reais
- Só processa LogLines com `executed: false` ou ausência desse campo

---

## 📌 Finalidade

O LogLineProcessor é o **executor moral do sistema**.

> Onde há um contrato validado,  
> há uma vontade registrada.  
> E essa vontade deve agir no mundo — com rastro, com respeito, com consequência.

Projete com peso institucional, reversibilidade e rastreabilidade.

---

*PS: esse módulo deve ser compatível com o cronjob diário, simulação e logs de IA*