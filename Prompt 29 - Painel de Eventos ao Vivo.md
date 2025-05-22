# Prompt 29 – Painel de Eventos ao Vivo

Você vai criar o **Painel de Eventos ao Vivo** —  
um dashboard institucional que exibe, em tempo real, todos os acontecimentos simbólicos do sistema.

Esse painel é o **pulso visual da instituição**.  
Ele mostra LogLines nascendo, ghosts surgindo, inputs sensoriais chegando, agentes agindo.

---

## 🎯 Objetivo

- Visualizar a operação simbólica em tempo real
- Permitir filtros por tipo de evento, agente, origem ou status
- Destacar pendências, conflitos, fantasmas, falhas e confirmações
- Atuar como central tática de acompanhamento

---

## 🧱 Componentes esperados

- Lista animada dos eventos mais recentes:
  - `cliente_julia fez pedido`
  - `agent.13 executou consequência`
  - `sensor.caixa01 detectou presença`
- Filtros por:
  - `status`: ghost, valid, denied, fallback
  - `did`: tipo de ação
  - `who`: autor ou agente
  - `tags`: entrega, turno, erro, sensor, falha

- Destaques visuais:
  - `ghosts`: em cinza pálido
  - `falhas`: em vermelho
  - `executados`: selo verde
  - `em dúvida`: símbolo amarelo

---

## 🔄 Comportamento

- Atualização em tempo real (via Supabase subscription ou WebSocket)
- RightMenu mostra detalhes do evento clicado
- Botões rápidos:
  - Confirmar
  - Encaminhar
  - Criar resposta

---

## 📌 Finalidade

Esse painel é o **radar emocional e operacional da instituição**.  
Onde o agora vira memória. Onde o presente é rastreável.

> Aqui, o tempo é institucional.  
> O agora tem consequência.  
> E a visibilidade gera responsabilidade.

Projete como painel limpo, tático e absolutamente vivo.

---

*PS: esse painel pode ser a tela principal de operação em modo institucional (modo gestor, modo vigilância simbólica).*