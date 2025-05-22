# RAG e Cache Semântico

## RAG com Supabase e LangChain

```python
from langchain.embeddings import OpenAIEmbeddings
from supabase import create_client

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
embeddings = OpenAIEmbeddings()

def index_logline(logline):
    vector = embeddings.embed_query(logline["this"])
    supabase.table("loglines").update({"vector": vector}).eq("id", logline["id"]).execute()
```

## Cache Semântico

- Cada resposta gerada por LLM deve ser armazenada com:
  - hash do prompt
  - modelo usado
  - vetor embutido da pergunta
- IA deve primeiro consultar o cache vetorial antes de gerar nova resposta

## LogLine de cache:

```json
{
  "who": "llm.cache",
  "did": "respondeu_por_cache",
  "refer_to": "logline_087",
  "model_used": "claude-3-sonnet",
  "status": "valid"
}
```