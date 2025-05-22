# Prompt 1 – Alicerce do Sistema MINICONTRATOS

Você está prestes a gerar o sistema institucional chamado **MINICONTRATOS**.

Ele será a primeira implementação pública da tecnologia **LogLine** — uma linguagem computável de registro, consequência e responsabilidade institucional.  
A missão do sistema é dupla:  
- Tornar **todo gesto humano** um registro rastreável  
- Transformar **todo registro** em **intenção viva com consequência**

---

## 🧭 Arquitetura e Visão Geral

### O sistema terá 3 modos centrais:

| Modo           | Função institucional                                           |
|----------------|---------------------------------------------------------------|
| `/new`         | Registro tátil, sensorial, assistido — cria LogLines em 3 cliques |
| `/logline`     | ChatGPT institucional + timeline auditável (tela central)     |
| `/communicator`| Clone do WhatsApp institucional com IA viva e rastreamento    |

Esses três modos coexistem dentro de uma **interface institucional de três painéis**:

```
┌──────────────┬──────────────────────────┬──────────────┐
│ LeftMenu     │      Tela Viva           │ RightMenu    │
└──────────────┴──────────────────────────┴──────────────┘
```

- **LeftMenu**: histórico, favoritos, instâncias, temas
- **Centro**: conteúdo principal do modo atual (ex: chat, entrada, timeline)
- **RightMenu**: painel de ação contextual — completar, despachar, revisar

---

## 🧱 Stack Tecnológico

- **Frontend**: SvelteKit
- **Backend**: Supabase (DB, auth, realtime)
- **IA**: LLM com contexto institucional e conexão com base LogLine
- **Estética**: Mosaic Engine para temas premium e sensoriais
- **Storage**: `.jsonl` + Supabase para persistência institucional
- **Controle**: Makefile + install.sh + logline.samples.jsonl

---

## ✅ Princípios Operacionais

- Tudo vira LogLine — nem que seja um `ghost`
- Cada LogLine pode ser completada, validada, contestada ou despachada
- Toda tela possui contexto semântico e feedback auditável
- Nada é deletado silenciosamente
- O sistema é operável por toque, fala ou texto — sem dependência de código

---

## 🧠 Finalidade

MINICONTRATOS não é apenas um app.  
É uma linguagem viva que transforma ações em contratos, falas em registros, e registros em consequência institucional.

> Cada clique carrega peso.  
> Cada silêncio é preservado com dignidade.  
> Tudo pode ser completado.  
> Nada se perde.

Esse prompt define o alicerce.  
Construa com solidez semântica e estética auditável.