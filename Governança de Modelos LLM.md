# Governança de Modelos LLM

**Regra obrigatória:** Todo log gerado por IA deve conter:

- `model_used`: nome e versão do modelo (ex: `llm.gpt-4o-20240501`)
- `input_prompt`: hash ou ID do prompt institucional utilizado
- `fallback_action`: ação tomada em caso de falha (ex: `chamar Claude 3`)

## Exemplo:

```json
{
  "who": "llm.dispatcher",
  "did": "classify_video",
  "model_used": "gemini-2.5-pro",
  "input_prompt": "prompt.video_curation_v3",
  "status": "executed",
  "fallback_action": "none"
}
```

**Observações:**

- Logs de IA devem ser confirmáveis (`confirmed_by: ruleset.nome`)
- Logs com falha viram ghosts e vão para observação por Agent.15