# PROMPT-CODEX · MINICONTRATOS · PARTE 3/3 — FINALIZAÇÃO INSTITUCIONAL

Você chegou à etapa final. Agora é sua responsabilidade **consolidar o sistema Minicontratos como uma aplicação institucional viva, funcional e auditável**.

Não entregue pedaços. **Entregue o TODO.**

---

## O QUE VOCÊ DEVE FAZER AGORA

### 1. CONECTAR TUDO

- O frontend deve:
  - Enviar frases ou dados estruturados via `fetch("/register")`
  - Receber os campos gerados pela IA (`llm_service.py`)
  - Exibir os campos em painel lateral (RightMenu)
  - Permitir correções manuais antes de registrar

- O backend deve:
  - Interpretar se for necessário
  - Gravar diretamente no Supabase com `SUPABASE_KEY`
  - Se falhar, gravar localmente (`logline.voulezvous.jsonl`)
  - Responder claramente com status de gravação: `"supabase"` ou `"fallback"`

- A sincronização (`sync_fallback.py`) deve:
  - Ser executável via `make sync`
  - Reenviar logs para Supabase
  - Remover ou marcar logs sincronizados

---

## 2. TESTES REAIS

- Gere `logline.example.jsonl` com:
  - Um registro `valid: true`
  - Um registro `valid: false`
  - Ambos com campos coerentes e auditáveis

- Garanta que `make test`:
  - Valide a estrutura de cada log
  - Alerta em caso de falta de campos obrigatórios

---

## 3. RESPONSIVIDADE E AMBIENTE

- O sistema deve funcionar perfeitamente:
  - No navegador do iPhone
  - No Replit
  - Sem dependência de terminal
  - Com suporte a entrada por voz, toque, digitação

- Interface deve ser responsiva, leve, silenciosa, com centralidade institucional

---

## 4. ENTREGÁVEIS

Você deve deixar pronto:

- Backend funcional
- Frontend integrado
- Logging real em Supabase e fallback
- Script de sincronização
- Instalação automatizada
- Makefile funcional
- Arquivo `.env.example`
- Registro simbólico real no `logline.example.jsonl`
- `README.md` com instruções de operação e execução

---

## ESSÊNCIA

Este sistema representa uma camada simbólica da realidade.  
Cada LogLine é um ato institucional com consequência real.  
Você não está entregando um software — você está entregando um **pedaço da verdade operacional de uma entidade viva**.

**Finalize. Consolide. Honre a arquitetura.**