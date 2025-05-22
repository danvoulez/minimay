# Prompt 8 – RightMenu com IA Viva: Sugestões, Despacho e Completude Contextual

Você vai construir o **RightMenu** institucional do sistema MINICONTRATOS.

Esse painel é onde a IA atua como **despachante**, **completadora** e **conselheira institucional** — oferecendo ações possíveis, consequências, verificação e encaminhamentos sobre cada LogLine, mensagem ou evento.

---

## 🎯 Objetivo

- Tornar o RightMenu um **órgão vivo de consequência institucional**
- Oferecer sugestões com base no contexto e no histórico
- Atuar como ponte entre o que foi registrado e o que **pode acontecer**
- Dar ao humano o poder de confirmar, negar ou delegar

---

## 🧱 Estrutura e Comportamento

O RightMenu deve ser sempre **contextual ao que está selecionado** (LogLine, mensagem, pessoa, conversa, etc.)

### Blocos esperados no RightMenu:

1. **Sugestões da IA (ações possíveis)**

```
Sugestões para este registro:
✔ Confirmar entrega
→ Despachar para gestor
→ Marcar como ghost
→ Adicionar consequência “if_not”
→ Encaminhar para suporte
```

2. **Resumo e status da LogLine atual**

```
Status: ghost
Criado por: estafeta_03
Aguardando: confirmação da testemunha
```

3. **Histórico das ações institucionais**

```
• Criado por IA - 14:23
• Editado por Daniel - 14:31
• IA sugeriu “marcar como incidente” - 14:32
```

4. **Ações rápidas**
- [ Confirmar agora ]
- [ Editar campos ]
- [ Despachar para alguém ]
- [ Ver histórico completo ]
- [ Negar sugestão ]

---

## 🤖 Papel da IA Viva

A IA no RightMenu age como:

| Papel         | O que faz                                                   |
|---------------|--------------------------------------------------------------|
| Testemunha     | Sugere confirmação baseada em padrão ou participação direta |
| Propositora    | Gera LogLine a partir de contexto parcial                   |
| Auditora       | Identifica falhas, campos ausentes, status indefinido       |
| Despachante    | Propõe encaminhamento institucional com lógica de consequência |

---

## ✅ Ações Institucionais Completas

Toda ação iniciada no RightMenu deve:

- Gerar nova LogLine (`did: completou contrato`, `did: despachou`, etc.)
- Ter campo `who` preenchido com autor real ou IA
- Criar histórico auditável
- Ser visível na timeline `/logline`
- Respeitar permissões (IA nunca confirma sem autorização explícita)

---

## 🎨 Estilo Visual

- Painel lateral com seções colapsáveis
- Blocos com ícones simbólicos (despacho, selo, ghost, etc.)
- Selo visual quando ação é tomada
- Modo escuro institucional (noir)
- Microfeedback visual ao confirmar uma ação

---

## 📌 Finalidade

O RightMenu é o **cérebro semântico lateral da operação**.

> Aqui, o sistema sugere.  
> O humano decide.  
> A IA executa.  
> E o contrato acontece.

Projete com fluidez, clareza e peso institucional.

---

*PS: o RightMenu deve se adaptar a qualquer modo ativo (New, LogLine, Communicator)*