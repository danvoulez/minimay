# Prompt 17 – GhostView Refinada (Tela de Rascunhos, Dúvidas e Sinais Incompletos)

Você vai construir a versão definitiva do **GhostView** — a tela onde vivem os registros incompletos, os contratos não finalizados, as dúvidas que ainda não viraram certeza.

Essa tela representa o **submundo legítimo da operação institucional**, onde o sistema dá dignidade à incompletude e cria espaço para regularização, questionamento ou descarte simbólico.

---

## 🎯 Objetivo

- Exibir todas as LogLines com `valid: false` (ghosts)
- Separar por tipo: falhas, dúvidas, rascunhos, sugestões da IA
- Permitir regularização manual ou automática
- Exibir idade do ghost, relevância e urgência de completar

---

## 🧱 Estrutura esperada

```
┌──────────────┬───────────────────────────────┬──────────────┐
│ LeftMenu     │     GhostView Refinada         │ RightMenu    │
└──────────────┴───────────────────────────────┴──────────────┘
```

### Bloco de cada ghost:

- Exibe campos preenchidos + campos faltantes
- Mostra `who`, `did`, `this`, `status`, tempo de criação
- Selo: “incompleto”, “pendente”, “cadastro fantasma”, “ação sugerida”
- Botões: `[Regularizar]`, `[Descartar]`, `[Reencarnar]`, `[Enviar para IA]`

---

## 🧠 Modos de visualização

- **Modo IA**: sugestões da Agent.15 para completar automaticamente
- **Modo Timeline Invertida**: ghosts mais antigos primeiro
- **Modo Ação Pendente**: ghosts que impediram execução de consequência
- **Modo Sensorial**: exibe fotos, áudios e gestos sem contrato final

---

## 🔄 Integrações

- Agent.15 propõe completudes em tempo real
- Agent.14 pode bloquear ações baseadas nesses ghosts
- RightMenu propõe transformar ghost em contrato válido
- IA pode preencher automaticamente os campos ausentes

---

## 📌 Finalidade

O GhostView não é uma lixeira.  
É um **espaço de honra para aquilo que ainda não está completo**, mas foi registrado com intenção.

> O que ainda não se tornou contrato...  
> ainda pode se tornar.  
> O que foi só um gesto...  
> já é uma promessa.

Projete com compaixão simbólica, rastreabilidade e capacidade de regularização fluida.

---

*PS: Ghosts nunca desaparecem — mas podem mudar de forma. Tudo aqui é reversível, simbólico e vivo.*