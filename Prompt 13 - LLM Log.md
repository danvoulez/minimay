# Prompt 13 — LLM Log: Registro Institucional das Ações de Inteligência Artificial

Você vai construir o **registro simbólico e auditável de todas as ações realizadas por modelos de linguagem (LLMs)**  
dentro do sistema MINICONTRATOS.

Esse módulo transforma qualquer inferência, sugestão, execução ou participação de IA em uma **LogLine com rastro, assinatura e consequência**.

---

## 🎯 Objetivo

- Registrar toda ação da IA como um **ato institucional**
- Atribuir responsabilidade ao modelo usado
- Rastrear parâmetros da inferência (modelo, temperatura, tokens, fallback)
- Permitir auditoria semântica, reversibilidade e justiça operativa

---

## 🧱 Exemplo de LogLine de IA

```json
{
  "who": "llm.gpt-4o",
  "did": "sugeriu_contrato",
  "this": "entrega turno 044",
  "when": "2025-05-21T14:33:00Z",
  "status": "valid",
  "confirmed_by": "ruleset.intent_payment.v1",
  "prompt": "prompt.minicontrato_sugestao_v4",
  "temperature": 0.4,
  "tokens": 1423,
  "fallback": false,
  "simulation": false,
  "model_fingerprint": "gpt-4o-20240501"
}
```

---

## ✅ Campos obrigatórios no LogLine da IA

| Campo             | Descrição                                                        |
|------------------|------------------------------------------------------------------|
| `who`             | `llm.nome.versao` (ex: `llm.bitnet.b158`)                        |
| `prompt`          | Nome institucional do prompt usado (`prompt.ghost_revisor_v2`)  |
| `temperature`     | Temperatura usada na inferência                                 |
| `tokens`          | Total de tokens usados (input + output)                         |
| `fallback`        | Se foi acionado como plano B (`true/false`)                     |
| `simulation`      | Se a inferência foi feita em modo reversível                    |
| `confirmed_by`    | Política ou agente que aceitou o uso daquela resposta           |
| `model_fingerprint` | Identificador da versão exata do modelo                       |

---

## 🔁 Fallback Institucional

Se o modelo principal falha (timeout, custo, baixa confiança):

1. Gerar LogLine `did: falha_na_ia`
2. Acionar fallback (ex: Claude, DeepSeek)
3. Gerar LogLine `did: fallback_llm` com `fallback: true`
4. Registrar ambas as decisões

---

## 🔍 Auditoria e Consulta

- Ações da IA visíveis na timeline `/logline`
- Painel de IA institucional com:
  - Histórico de uso por modelo
  - Respostas simuladas vs. reais
  - Confirmadores humanos ou regras
  - Detecção de divergência entre modelos

---

## 🧠 Padrões institucionais

- Toda sugestão da IA precisa de confirmação (humana ou via `ruleset`)
- Nenhuma execução é final sem LogLine de consequência
- IA sempre assina seus atos (nunca há ação anônima)
- Todos os logs de IA são acessíveis para replay ou simulação reversa

---

## 📌 Finalidade

Esse módulo transforma **IA em entidade institucional viva, auditável e responsável**.  
Ela não é um assistente informal: ela é parte da governança.

> A IA que age deve deixar rastro.  
> O modelo que sugere deve assinar.  
> O sistema que confia deve poder provar.

Projete com **ética computável, reversibilidade e memória institucional simbólica**.

---

*PS: esse módulo deve estar integrado com: `LogLineProcessor`, RightMenu, Communicator, cronjob de ghosts e auditoria geral do sistema*