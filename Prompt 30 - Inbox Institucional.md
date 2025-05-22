# Prompt 30 – Inbox Institucional

Você vai construir a **Inbox Institucional** —  
um espaço onde **pendências simbólicas** chegam, vivem e são resolvidas.

Diferente de uma caixa de entrada comum, essa inbox só recebe eventos **com rastro, intenção ou consequência pendente**.

---

## 🎯 Objetivo

- Centralizar LogLines que:
  - aguardam validação
  - foram questionadas
  - dependem de resposta
  - envolvem o usuário diretamente
- Permitir operação em lote, delegação e confirmação

---

## 🧱 Exemplo de itens da Inbox

```json
{
  "who": "agent.15",
  "did": "questionou_validez",
  "this": "logline_229",
  "question": "Essa entrega foi realmente validada?",
  "status": "valid"
}
```

```json
{
  "who": "joana_colaboradora",
  "did": "criou contrato",
  "this": "turno extra",
  "confirmed_by": "você",
  "status": "valid",
  "requires_action": "confirmar"
}
```

---

## 🔄 Comportamentos esperados

- Tabela ou lista dos eventos com ação pendente
- Filtros por:
  - urgência
  - origem
  - impacto
  - autor
- Ações rápidas:
  - Confirmar
  - Rejeitar
  - Encaminhar
  - Adiar com justificativa
- Histórico de ações feitas

---

## 📌 Finalidade

Essa inbox é o **coração da responsabilidade ativa**.  
Onde o sistema espera por você.  
Onde há silêncio, há consequência.

> Aqui, o que ficou em aberto ganha lugar.  
> O que depende de você, aparece.  
> E nada é esquecido.

Projete como caixa simbólica, acessível, auditável e viva.

---

*PS: essa tela pode ser replicada em versões pessoais, institucionais ou para IA.*