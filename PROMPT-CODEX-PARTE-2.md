# PROMPT-CODEX · MINICONTRATOS · PARTE 2/3 — FRONTEND INSTITUCIONAL

Você é responsável por criar o frontend do sistema institucional **Minicontratos**, utilizando **SvelteKit**.

Este frontend não é uma interface comum — ele representa **a camada sensorial e simbólica da operação institucional**.

---

## OBJETIVO DO FRONTEND

- Apresentar ao operador humano uma forma intuitiva, silenciosa e auditável de registrar acontecimentos reais
- Integrar os três modos de entrada:
  1. **LogLine** (entrada livre com IA)
  2. **Communicator** (conversa com IA viva)
  3. **New / Contracter** (formulário tátil de minicontratos)

---

## TAREFAS PARA VOCÊ EXECUTAR AGORA

### 1. ESTRUTURA VISUAL

- Use SvelteKit no diretório `frontend/`
- Crie os componentes necessários:
  - `LogLineView.svelte`
  - `CommunicatorView.svelte`
  - `ContracterView.svelte`
  - `RightMenu.svelte` (painel institucional de campos)
  - `LeftMenu.svelte` (menu de navegação entre modos)

- Centralize todos os modos dentro de um layout principal:
  - Navegação por toque no `LeftMenu`
  - Exibição de conteúdo central (modo ativo)
  - Ações, validação e campos no `RightMenu`

### 2. FUNCIONALIDADE

- O campo “o que aconteceu?” deve:
  - Estar presente em todos os modos
  - Permitir digitar ou colar texto
  - Suportar entrada por voz (via atributo `speech-to-text` ou Web API)

- Carregue sugestões de `prompts.extended 2.json` e exiba dinamicamente
- Ao registrar:
  - envie a frase para `/register` via `fetch`
  - receba os campos interpretados pela IA
  - preencha o RightMenu com os dados
  - permita revisar e confirmar antes de registrar

- Feedback visual:
  - Sucesso (registrado no Supabase)
  - Fallback (salvo localmente)
  - Erro (problemas com rede ou IA)

---

### 3. REQUISITOS DE INTERFACE

- Visual limpo, sem logos, sem textos explicativos
- Foco em gesto, toque e resposta sensorial
- Deve funcionar perfeitamente no navegador do iPhone
- Adaptável a Replit com preview ativado
- Suporte a modo PWA (Progressive Web App) opcional

---

## ENTREGA ESPERADA

Ao concluir essa parte, o sistema deve:

- Ser usável pelo humano sem orientação
- Exibir respostas da IA de forma auditável
- Permitir correção manual dos campos antes de registrar
- Gerar logs com peso institucional a partir da interface

Este frontend representa o “rosto visível” da verdade registrada.

**Você deve construí-lo com clareza, fluidez e respeito semântico.**