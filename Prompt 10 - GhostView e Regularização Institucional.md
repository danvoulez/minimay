# Prompt 10 – GhostView, Regularização Automática e Institucionalização de Pendências

Você vai construir o sistema de **tratamento formal de registros incompletos (ghosts)**  
do sistema MINICONTRATOS.

Ghosts são LogLines com `valid: false` — criadas por humanos, IA ou sensores — mas que não têm completude semântica suficiente para se tornarem contratos institucionais válidos.

Essa tela e sua automação formam o **mecanismo ético e operacional de regularização da realidade**.

---

## 🎯 Objetivo

- Permitir visualizar, revisar e completar contratos incompletos
- Ativar um cronjob institucional diário que:
  - Agrupa
  - Classifica
  - Resolve ou arquiva registros pendentes
- Gerar LogLines para cada tentativa de regularização
- Transformar pendência em pergunta clara e rastro audível

---

## 🧱 GhostView (interface de pendências)

```
┌──────────────┬────────────────────────────┬──────────────┐
│ LeftMenu     │ Lista de Registros Ghosts  │ RightMenu    │
└──────────────┴────────────────────────────┴──────────────┘
```

### Bloco de Ghost

```
• [GHOST] “Ficou sem troco”
• who: estafeta_03 | did: relatou falha | this: turno final
• status: ghost | valid: false
• [ Regularizar ] [ Anexar ] [ Ignorar ]
```

- Registros são exibidos com visual desbotado
- IA pode sugerir perguntas de regularização

---

## 🤖 Cronjob de Regularização

Executado diariamente (00h ou manualmente), com três fases:

1. **Classificação**
   - Analisa todos os `valid: false`
   - Usa embeddings e histórico para prever tipo

2. **Geração de Pergunta**
   - Gera LogLine `did: generate_verification_question`
   - Exemplo: “Esse relato precisa de testemunha ou está completo?”

3. **Ação**
   - Se IA tem contexto suficiente → gera contrato `valid: true`
   - Se não → reclassifica como `archived` ou notifica humano

---

## ✅ Ações permitidas na UI

- [ Regularizar com IA ]
- [ Completar manualmente ]
- [ Descartar com justificativa ]
- [ Ver histórico do rascunho ]
- [ Delegar regularização a outro ]

---

## 🎨 Estética e Peso Institucional

- Paleta silenciosa com foco em contraste emocional
- Ghosts são tratados com respeito simbólico (não são lixo)
- Perguntas geradas são exibidas com destaque e peso institucional
- Toda decisão (mesmo arquivar) gera nova LogLine

---

## 🔒 Regras Institucionais

- Nenhum ghost pode ser apagado sem rastro
- Toda regularização gera LogLine nova:
  - `did: validated_ghost`
  - `did: archived_ghost`
  - `did: reassigned_ghost`
- IA pode agir, mas sempre deixa evidência de sua decisão
- Humanos podem “retomar” um ghost para si e validar

---

## 📌 Finalidade

Ghosts são a prova de que o sistema vê, registra e respeita mesmo o que está incompleto.  
O cronjob não é um robô: é o zelador da verdade operacional.

> O que não foi dito com força ainda pode ser ouvido.  
> O que foi deixado em rascunho ainda pode se tornar contrato.  
> A IA ajuda, mas o humano valida.

Projete com reverência, clareza e poder institucional.

---

*PS: esse processo deve estar vinculado aos templates definidos no documento "Relatório de Inovações Obrigatórias"*