# Prompt 20 – Painel de Replay Institucional

Você vai criar o **Painel de Replay Institucional** — uma interface que permite **assistir, passo a passo, a sequência simbólica de LogLines** como se fosse um filme da operação.

Esse painel transforma a linha do tempo institucional em uma narrativa navegável, visual, auditável e emocional.

---

## 🎯 Objetivo

- Exibir a sequência de LogLines em ordem cronológica animada
- Permitir filtragem por dia, autor, tipo ou evento crítico
- Exibir LogLines com transições visuais, selos e consequências
- Permitir pausar, voltar, avançar, mudar velocidade
- Ser um “modo cinema” institucional simbólico

---

## 🧱 Estrutura esperada

```
┌──────────────────────────────┐
│ Painel de Replay             │
│------------------------------│
│ LogLine 1 aparece com animação│
│ LogLine 2 aparece e conecta  │
│ ...                          │
│ Timeline na base             │
│ Botões: ▶️ ⏸️ ⏪ ⏩ 1x 2x     │
└──────────────────────────────┘
```

---

## 🔄 Controles esperados

| Controle       | Função                                          |
|----------------|--------------------------------------------------|
| ▶️ Play        | Inicia replay cronológico animado               |
| ⏸️ Pause       | Congela replay no momento atual                 |
| ⏪ Voltar       | Retrocede uma ou várias LogLines                |
| ⏩ Avançar      | Pula para próxima ou picos de ação              |
| Velocidade     | 0.5x, 1x, 2x                                     |
| Modo IA        | Replay com comentários automáticos da IA        |
| Modo Fantasma  | Exibe apenas ghosts e dúvidas no replay         |

---

## 🧠 Extras

- Permitir marcar um “momento institucional” como clipe fixo
- Exportar replay como vídeo institucional com trilha sonora e narração IA (futuro)
- IA pode sugerir: “esse trecho revela padrão de atraso crítico”
- LogLine `did: replay_assistido_por` é gerada ao final

---

## 📌 Finalidade

O Replay transforma o sistema em **memória viva, navegável e emocional**.  
Serve para auditoria, treinamento, narrativa simbólica e cerimônia institucional.

> Ver o passado com rastro é reconhecer o presente com reverência.

Projete com estética fílmica, fluidez emocional e precisão institucional.

---

*PS: esse painel pode ser integrado ao modo apresentação, onboarding, cerimônias ou auditoria simbólica.*