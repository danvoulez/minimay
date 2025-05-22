# FlipApp

Sistema para registrar eventos em formato LogLine e salvar no Supabase ou fallback local.

## Instalação

```bash
make install
```

## Uso

Execute o backend Flask:

```bash
python backend/app.py
```

Acesse o frontend em `frontend` usando SvelteKit (`npm run dev`).

Para sincronizar eventos do fallback:

```bash
make sync
```

Execute testes:

```bash
make test
```

