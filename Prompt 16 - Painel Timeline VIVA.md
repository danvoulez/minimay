# Prompt 16 – Painel Timeline VIVA

Você vai construir a **tela principal de navegação institucional** do sistema Minicontratos.  
É o lugar onde **tudo que aconteceu pode ser visto, filtrado, compreendido e reencarnado**.  
A Timeline VIVA é a memória simbólica da operação — **a linha do tempo de contratos e consequências**.

---

## 🎯 Objetivo

- Exibir LogLines com clareza emocional e institucional
- Permitir visualização por:
  - Lista cronológica
  - Timeline simbólica com barras, selos e rastro
  - Grade agrupada por tipo, status, impacto ou pessoa
- Integrar com RightMenu para ações imediatas
- Exibir animações de desdobramento, conflito ou dúvida

---

## 🧱 Estrutura esperada

```
┌──────────────┬───────────────────────────────┬──────────────┐
│ LeftMenu     │   Timeline VIVA (dinâmica)    │ RightMenu    │
└──────────────┴───────────────────────────────┴──────────────┘
```

### Blocos principais:

- Cada LogLine vira um cartão visual:  
  → `“Entregou caixa 014 | estafeta_09 | valid | 14h32”`  
- Selo de status: `valid`, `ghost`, `denied`, `conflict`, `auto`
- Ícones para `if_ok`, `if_not`, `if_doubt`
- Botões: `[Ver mais]`, `[Aprofundar]`, `[Desdobrar]`, `[Enviar]`

---

## 🔍 Filtros e Modos

- Filtro por campos: `who`, `did`, `this`, `status`, `tags`, `confirmed_by`
- Modo Ghost: exibe apenas rascunhos e incompletos
- Modo Ação: exibe apenas LogLines com consequência pendente
- Modo Agente: filtra ações por agentes (13, 14, 15)

---

## 🔄 Interações vivas

- Scroll infinito
- Animações quando nova LogLine entra
- Timeline pulsa se algo precisa ser resolvido
- Ghosts aparecem com brilho desbotado e selo “incompleto”
- LogLines com desdobramentos ganham botão de expansão

---

## 📌 Finalidade

A Timeline VIVA é a **memória visível da instituição viva**.  
Tudo o que aconteceu — e o que ainda precisa acontecer — está aqui.

> O que foi feito, respira.  
> O que falta, pulsa.  
> O que é contrato, vive.

Projete com beleza, velocidade e sentido institucional claro.

---

*PS: essa tela é o coração visual do sistema, usada por todos os papéis. A Timeline é o ponto de partida e o ponto de retorno.*