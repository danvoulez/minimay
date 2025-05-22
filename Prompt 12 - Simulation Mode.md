# Prompt 12 – Simulation Mode: Execução Institucional Sem Efeito Real

Você vai construir o **modo de simulação oficial do sistema MINICONTRATOS**.  
Esse modo permite testar, demonstrar, validar e visualizar contratos **sem produzir efeitos reais**, mas com rastreabilidade e feedback.

---

## 🎯 Objetivo

- Permitir que qualquer ação, LogLine, consequência ou sequência seja testada com rastro
- Criar um ambiente isolado para desenvolvimento, onboarding e treinamento
- Garantir que **nenhuma consequência real** seja executada, mas que todas as etapas sejam logadas

---

## 🧱 Como funciona

- Toda LogLine criada em modo simulação carrega:

```json
"simulation": true
```

- Toda consequência (`if_ok`, `if_doubt`, `if_not`) será **interpretada e registrada**, mas:
  - Não dispara APIs externas
  - Não altera estado real
  - Pode disparar callbacks visuais, testes ou logs de simulação

---

## 🔁 Comportamento esperado

- `LogLineProcessor` reconhece `simulation: true` e atua em **modo reversível**
- RightMenu exibe selo visual: “SIMULAÇÃO – sem consequência real”
- Timeline agrupa logs simulados com destaque simbólico
- Feedback visível em cada ação: “Essa execução foi simulada”

---

## ✅ Casos de uso

- Onboarding de novos membros
- Teste de prompts LLM
- Validação de regras sem risco
- Reencenação de incidentes passados
- Demonstração de funcionamento para terceiros

---

## 🧾 Exemplo de LogLine simulada

```json
{
  "who": "daniel",
  "did": "registrou entrega",
  "this": "turno_44",
  "status": "valid",
  "if_ok": "liberar_pagamento",
  "simulation": true
}
```

---

## 📊 Visual e Integração

- Painel superior ou inferior com aviso fixo: “Modo Simulação Ativo”
- Opção de exportar logs simulados
- Botão “Repetir no mundo real” (remove `simulation`, gera nova LogLine)

---

## 🔐 Regras institucionais

- Nenhum LogLine simulado pode ser validado como oficial
- Nenhuma ação em modo simulação pode alterar saldo, estados ou bancos reais
- Todas as execuções simuladas devem ser registradas como tal (`did: simulou_consequencia`)

---

## 📌 Finalidade

Esse é o **ambiente seguro da instituição**.  
É onde o sistema aprende com seus próprios contratos.  
É onde falhar não tem custo, mas o aprendizado tem valor.

> A simulação é o futuro sendo ensaiado com dignidade.  
> Nenhum dano. Todo rastro. Toda sabedoria.

Projete com respeito, clareza e rastreabilidade simbólica.

---

*PS: esse modo deve ser respeitado por todos os módulos: LogLineProcessor, Communicator, LLM Gateway, cronjobs e RightMenu*