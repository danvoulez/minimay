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

## Sincronização

Para sincronizar eventos do fallback com o Supabase:

```bash
make sync
```

## Testes

Para executar os testes:

```bash
make test
```

## Contribuição

Para contribuir com o projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
