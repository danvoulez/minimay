# Prompt 2 – Estrutura do Repositório MINICONTRATOS (Ex-Flip App)

Você é responsável por gerar a estrutura completa do repositório **MINICONTRATOS** —  
um sistema institucional mobile-first que registra, exibe e valida eventos com linguagem LogLine.

Este repositório deve funcionar como um **ambiente de missão institucional**, com foco em:

- Rastreabilidade (cada evento é um log)
- Redundância simples (tudo salvo local + Supabase)
- Deploy sem dor (um clique no Vercel ou Supabase)
- Navegação fluida entre painéis: histórico, conteúdo, ação
- Código compreensível por humanos normais

---

## 🧱 Estrutura Esperada

```
minicontratos/
├── src/
│   ├── lib/
│   │   ├── supabaseClient.ts          # Conexão com Supabase
│   │   ├── logline.ts                 # Helpers para criação e parsing de LogLines
│   │   ├── ghost.ts                   # Guardião institucional dos registros incompletos
│   │   └── ai.ts                      # Placeholder de integração com IA corretora
│   ├── app.d.ts                       # Tipos globais (Supabase, LogLine, User)
│   ├── routes/
│   │   ├── +layout.svelte             # Shell com LeftMenu, RightMenu e painel central
│   │   ├── +page.svelte               # Redireciona para /new
│   │   ├── new/+page.svelte           # Tela para registrar o que aconteceu
│   │   ├── logline/+page.svelte       # Timeline + chat institucional
│   │   └── communicator/+page.svelte # Chat com IA e pessoas
│   └── styles/
│       └── theme.css                  # Tokens do Mosaic Engine
├── static/
│   └── favicon.png
├── .env.example                       # Variáveis para Supabase e IA
├── README.md                          # Explica o sistema, as telas e o propósito
├── install.sh                         # Instala tudo e testa conexão
├── logline.samples.jsonl              # Linha do tempo simbólica de exemplo
└── makefile                           # Comandos úteis (dev, deploy, log, clean)
```

---

## 📌 Detalhes e Padrões

- A estrutura deve suportar o layout institucional:
  - **LeftMenu** para navegação pessoal e organizacional
  - **Centro** para chat, registros, ou fluxos ativos
  - **RightMenu** para ação contextual sobre LogLines (editar, despachar, completar)
- As rotas devem seguir nomes semânticos (`/new`, `/logline`, `/communicator`)
- `ghost.ts` deve exportar `isGhost(logline)` e `ghostReason(logline)` — usado em toda a UI e backend
- Todos os campos da LogLine são obrigatórios, mas o sistema deve aceitar incompletos
- O `install.sh` testa Supabase, ambiente e salva LogLine de boot com status institucional

---

## ✅ Princípios Estilo NASA

- Se algo falhar, o sistema **registra o erro como LogLine com `who: system`**
- Nunca deletar dados silenciosamente — apenas marcar como `ghost` ou `failed`
- Suporte a modo `"simulation"` para testes sem consequência real
- A linha do tempo (`logline.samples.jsonl`) é tratada como dado simbólico — nunca só exemplo
- Toda nova funcionalidade deve gerar uma LogLine de si mesma (`did: "criou novo modo"`)

---

## 🧠 Finalidade

Esse repositório não é só um app.  
Ele é o **sistema nervoso da operação institucional da VoulezVous**, acessível por toque, auditável por IA, e rastreável por qualquer operador.

Ele deve rodar com um clique, explicar-se com seus próprios logs e ser bonito de ver e leve de entender.

> Gera a estrutura com essa base.  
> Um operador humano deve conseguir abrir o repositório e saber o que é cada pasta sem depender de mágica.