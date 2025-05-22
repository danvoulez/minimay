# Prompt 19 – Ruleset Inspector (Painel Visual das Regras Institucionais)

Você vai criar o painel **Ruleset Inspector** — a interface onde as regras institucionais do sistema são visualizadas, testadas, ativadas ou suspensas.

Essas regras são o cérebro simbólico que valida, confirma, impede ou autoriza consequências automáticas.  
Esse painel é o **centro de governança semântica computável** da instituição.

---

## 🎯 Objetivo

- Exibir todas as regras (`ruleset.*`) ativas, suas funções e suas consequências
- Permitir visualização simbólica (nome, campo afetado, tipo de validação, últimas execuções)
- Permitir ativar/desativar regras
- Simular aplicação de uma regra sobre LogLines reais
- Ver histórico de aplicação (`who: ruleset.*`, `confirmed_by: ruleset.*`)

---

## 🧱 Estrutura esperada

```
┌──────────────┬───────────────────────────────┬──────────────┐
│ LeftMenu     │   Ruleset Inspector            │ RightMenu    │
└──────────────┴───────────────────────────────┴──────────────┘
```

### Bloco de cada regra

- Nome canônico: `ruleset.intent_payment.v1`
- Tipo: `validação`, `consequência`, `autorização`
- Campo afetado: `if_ok`, `status`, `confirmed_by`
- Última execução: data e LogLine
- Selo: ativo/inativo, criticidade, cobertura

---

## ✅ Ações permitidas

| Ação                | Efeito                                               |
|---------------------|-------------------------------------------------------|
| [Ativar]            | Torna a regra operativa imediatamente                |
| [Desativar]         | Suspende temporariamente sua aplicação               |
| [Testar]            | Permite simular regra em LogLine específica          |
| [Histórico]         | Abre LogLines onde ela foi aplicada                  |
| [Editar lógica]     | (futuro) Interface para ajustar a condição de regra  |

---

## 📊 Informações agregadas

- Quantidade de LogLines impactadas por cada regra
- Quantas foram `confirmadas`, `negadas`, `sugeridas`
- Pontuação simbólica: efetividade, dúvida, rejeição
- Representação visual: mapa de calor de uso por tipo de evento

---

## 📌 Finalidade

O Ruleset Inspector é o **tribunal computável da operação**.  
É onde cada decisão que não foi humana — precisa se justificar.

> Toda regra precisa ser visível.  
> Toda consequência automática, rastreável.  
> Toda decisão sem rosto, precisa de rastro.

Projete com clareza lógica, estética institucional e auditabilidade computável.

---

*PS: esse painel é protegido, acessível apenas por papéis institucionais com autoridade de regra.*