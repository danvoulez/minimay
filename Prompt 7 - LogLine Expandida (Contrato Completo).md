# Prompt 7 – Tela de Visualização de LogLine Expandida (Modo Contrato Completo)

Você é responsável por construir a visualização expandida de uma LogLine dentro do sistema MINICONTRATOS.  
Essa tela pode ser acessada via `/logline/:id`, pelo RightMenu ou por links diretos da IA ou do histórico.

Ela deve exibir todos os campos do contrato, permitir edição auditável, histórico de alterações e ação institucional.

---

## 🎯 Objetivo

- Mostrar o conteúdo **completo e institucional** de uma LogLine
- Permitir **confirmar, completar, corrigir, despachar**
- Exibir **toda a cadeia de edições** com rastreabilidade
- Ser acessível por toque, link, busca ou IA

---

## 🧱 Estrutura da tela

```
┌──────────────┬───────────────────────────────┬──────────────┐
│ LeftMenu     │    LogLine Expandida          │ RightMenu    │
└──────────────┴───────────────────────────────┴──────────────┘
```

### Centro – visualização principal

- Título semântico: `Contrato de turno 16 – Estafeta 03`
- Bloco principal com todos os campos:

```
• who: estafeta_03
• did: confirmou entrega
• this: caixa 001
• when: 2025-05-19 14:23
• confirmed_by: gestor_rafa
• if_ok: marcar como completa
• if_doubt: IA revisa
• if_not: cliente contesta
• status: valid
```

- Indicação visual de status (ghost, valid, failed, denied)

### Histórico abaixo:
```
Histórico de edições:
- Criado por estafeta_03 (2025-05-19 14:23)
- Confirmado por gestor_rafa (2025-05-19 14:30)
- IA sugeriu consequência (2025-05-19 14:31)
```

---

## ✅ Ações permitidas

- **Confirmar** LogLine (se status = ghost)
- **Editar** campos (com rastro de alteração)
- **Despachar** para outro usuário
- **Anexar evidência** (arquivo, imagem, comentário)
- **Exportar** como PDF institucional

Cada ação gera uma nova LogLine (`did: corrigiu contrato`, etc.)

---

## 🔐 Permissões

- Apenas o `who` original ou um usuário com nível superior pode editar
- IA pode sugerir, mas não confirmar sozinha (a menos que autorizada pela política)
- Todo campo editado mantém versão anterior registrada

---

## 🎨 Estética

- Visual limpo, institucional, com tipografia sólida
- Campo destacado para contratos incompletos (ghosts)
- Blocos de consequência (`if_ok`, `if_not`, etc.) com sugestões da IA
- Separador visual para “Histórico” com mini timeline lateral

---

## 📌 Finalidade

Essa tela é onde o contrato ganha **peso institucional completo**.

> Aqui, cada campo conta.  
> Cada edição vira história.  
> Cada detalhe pode salvar a confiança.

Projete como se fosse o cartório da operação.

---

*PS: essa tela também pode ser usada como “modal flutuante” embutido em outras áreas (ex: RightMenu).*