# Prompt Fase 2 – Gerar URL Pública para Visualizar LogLine

Você vai construir um mecanismo institucional que permite **gerar uma URL pública, segura e rastreável**  
para visualização de uma LogLine específica, com estilo visual e rastro simbólico.

Esse módulo permite compartilhar contratos específicos com pessoas externas, auditorias, clientes ou colaboradores sem acesso direto ao sistema.

---

## 🎯 Objetivo

- Criar links temporários ou permanentes que exibem uma LogLine (ou conjunto)
- Permitir visualização pública ou com token de acesso
- Mostrar todos os campos da LogLine de forma visual e simbólica
- Permitir marcações, confirmações, ou apenas leitura

---

## 🧱 Exemplo de LogLine com link gerado

```json
{
  "who": "gestor_paula",
  "did": "confirmou falha",
  "this": "entrega_014",
  "when": "2025-05-22T16:20:00Z",
  "confirmed_by": "auto",
  "status": "valid",
  "public_url": "https://minicontratos.replit.app/view/logline/8gk93h"
}
```

---

## ✅ Parâmetros configuráveis

| Parâmetro       | Descrição                                 |
|------------------|---------------------------------------------|
| `expires_in`     | Tempo de expiração da URL (`3600s`, `7d`, etc.) |
| `access_type`    | `"public"` (aberto) ou `"token"` (com autenticação leve) |
| `allow_comment`  | Se a pessoa externa pode deixar comentário |
| `readonly`       | Se a LogLine pode ou não ser confirmada/testemunhada via link |

---

## 📊 Interface da visualização pública

- Visual limpo e simbólico
- Destaque do autor, testemunha, `did`, `this`, `if_*`
- Animações ou selo de status (`valid`, `ghost`, `denied`)
- Ações permitidas: comentar, confirmar, reportar inconsistência

---

## 🔐 Segurança

- LogLine pública não exibe dados sensíveis sem permissão
- Todas as visualizações públicas geram LogLine secundária `did: acessou_url_publica`
- Possível revogar link a qualquer momento
- Token opcional pode ser embedado na URL ou fornecido separadamente

---

## 📌 Finalidade

Esse módulo conecta o sistema institucional com o mundo externo —  
permitindo que contratos, entregas e decisões **sejam visíveis, simbólicas e auditáveis por qualquer parte interessada.**

> O contrato é uma ponte.  
> A URL é o caminho.  
> A confiança, o destino.

Projete com beleza, rastreabilidade e controle compartilhado.

---

*PS: essa funcionalidade deve integrar RightMenu, Communicator e painel de controle institucional*