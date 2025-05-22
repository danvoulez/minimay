# PROMPT-CODEX · MINICONTRATOS · PARTE 1/3

Você é responsável por iniciar e estruturar o sistema institucional chamado **Minicontratos**.

Este sistema transforma frases como “entreguei o pedido” em um registro semântico institucional com os seguintes campos:

- who
- did
- this
- when
- confirmed_by
- if_ok
- if_doubt
- if_not
- status

Esses registros são chamados de **LogLines**, e formam a linha do tempo oficial de tudo que acontece na organização.

---

## PARTE 1 — CONFIGURAÇÃO E BASE

Sua missão nesta etapa:

### 1. BACKEND FLASK

- Verifique e finalize `backend/app.py`:
  - Rota POST `/register` que:
    - recebe frase ou JSON
    - usa `llm_service.py` para gerar os campos
    - grava no Supabase (via REST API com `SUPABASE_KEY`)
    - se falhar, grava localmente em `logline.voulezvous.jsonl`
  - Rota GET `/prompts` que retorna `prompts.extended 2.json`

- Finalize `llm_service.py` com função:
```python
def interpretar_frase(frase: str) -> dict:
    # deve retornar os 9 campos da LogLine
```

- Use `.env` com:
  - `SUPABASE_URL`
  - `SUPABASE_KEY`
  - `LOG_FALLBACK_PATH`

---

### 2. FALBACK E SINCRONIZAÇÃO

- Finalize `sync_fallback.py` para:
  - Ler `logline.voulezvous.jsonl`
  - Reenviar via Supabase REST
  - Remover linhas sincronizadas
- `make sync` deve executar esse script

---

### 3. ESTRUTURA E INSTALAÇÃO

- Crie ou finalize:
  - `install.sh`
  - `Makefile` com targets: run, sync, test, clean
- Confirme `.env.example` completo

---

### SAÍDA ESPERADA

Ao concluir esta parte:

- Backend deve aceitar registros
- Fallback deve funcionar
- Supabase deve estar integrado
- Sync deve estar ativável por `make`

Após isso, prossiga para a Parte 2 (Frontend e UI).