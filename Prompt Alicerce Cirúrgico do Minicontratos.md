Prompt Alicerce Cirúrgico do Minicontratos
Instrução direta, modular e operável para gerar a base viva do sistema

Papel da IA executora
Você é um agente técnico encarregado de construir o alicerce real do sistema Minicontratos, o primeiro aplicativo institucional da Tecnologia LogLine.
Seu objetivo é gerar um projeto mínimo, auditável, pronto para deploy, com os três modos vivos do Flip App: New, LogLine Viewer e Communicator.

Resumo do sistema
Nome do projeto: minicontratos

Linguagem principal: SvelteKit (framework institucional escolhido)

Backend: Supabase (PostgreSQL + Realtime)

Output principal: LogLines no padrão semântico oficial

Interface: silenciosa, tátil, modular e institucional

Tarefas obrigatórias deste prompt
Você deve gerar a estrutura inicial de arquivos, pastas e lógica base do sistema, com:

1. Setup base
Estrutura de projeto sveltekit

Integração com @supabase/supabase-js

.env com variáveis necessárias (SUPABASE_URL, SUPABASE_ANON_KEY)

Função central dispatch_logline(log: LogLine)

2. Roteamento modular por modo
/new: registro de minicontratos (input + botão + realtime)

/logline: visualização da linha do tempo (timeline de LogLines)

/chat: communicator tipo WhatsApp com IA ou mensagens

Cada rota é um componente isolado em /routes/[modo]/+page.svelte

3. LogLine real e canônico
Toda ação de envio ou clique deve gerar um objeto LogLine com os 9 campos obrigatórios

Campos faltantes tornam o log valid: false e status: ghost

Logs são enviados para a tabela loglines no Supabase

4. Detalhes técnicos a respeitar
Os logs devem conter:
who, did, this, when, confirmed_by, if_ok, if_doubt, if_not, status

Campos adicionais permitidos:
type, tags, valid, subsystem, details, source_file

Os logs devem ser enviados com supabase.from('loglines').insert([log])

O frontend deve escutar novos logs com .channel().on(...)

5. Estética e comportamento
Design tátil, sem texto explicativo

input minimalista com placeholder: o que aconteceu?

Botões silenciosos e auditáveis

Cada troca de modo (New, LogLine, Chat) deve gerar um LogLine com:

did: entrou modo

this: new / logline / chat

status: valid

O que este prompt não deve fazer
Não usar React, Vite, Webpack ou JSX

Não usar frameworks pesados ou estruturas difíceis de hospedar

Não registrar logs soltos ou sem consequência

Não usar APIs simuladas — tudo deve ser integrado com o Supabase real

Exemplo de LogLine esperada no envio de um minicontrato
json
Copiar
Editar
{
  "who": "danvoulez",
  "did": "registrou evento",
  "this": "cliente 203 pediu entrega urgente",
  "when": "2025-05-20T13:00:00Z",
  "confirmed_by": "auto",
  "if_ok": "acionar estafeta",
  "if_doubt": "enviar pergunta ao cliente",
  "if_not": "ignorar",
  "status": "valid",
  "type": "human",
  "tags": ["venda", "urgente"]
}
Meta do Prompt
Gerar a base do sistema Minicontratos real, funcional e institucional, pronta para receber os próximos prompts:

prompt.recheio: adiciona lógica interna, validação, feedback e IA

prompt.finalizacao: empacota, estiliza e prepara para deploy silencioso e confiável

Fim do Prompt 3 — Alicerce Cirúrgico
Pronto para ser executado por qualquer IA construtora com consciência institucional.

Se quiser, posso gerar agora o prompt.recheio como próximo passo. Deseja seguir?
