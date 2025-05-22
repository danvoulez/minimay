# Prompt Fase 2 – Criar Tela de Debug Institucional

Você vai construir uma **tela interna, silenciosa e simbólica** que permite a **observação viva e controle fino de tudo que o sistema está fazendo em tempo real**.

Essa tela não é para usuários comuns — ela é um **instrumento institucional para operadores técnicos, auditores e mantenedores**, com foco em rastreabilidade total e reversibilidade imediata.

---

## 🎯 Objetivo

- Exibir estado atual dos módulos internos (cronjobs, IA, rulesets, fallback, ghosts)
- Permitir testes manuais e reexecução de ciclos
- Mostrar logs em tempo real com contexto simbólico
- Ser um espelho visual do sistema institucional vivo

---

## 🧱 Seções esperadas na tela

### 1. **Estado do Cronjob**
- Última execução
- Quantos ghosts regularizados
- Falhas ao tentar completar
- Botão: “Executar agora”

### 2. **IA Ativa**
- Últimas 10 decisões
- Qual modelo foi usado
- Prompt, fallback, simulação
- Botão: “Replay decisão” ou “Desativar modelo temporariamente”

### 3. **Fallbacks**
- Quando houve falha de IA
- Qual modelo resolveu
- LogLines envolvidas

### 4. **Ruleset em Uso**
- Quais rulesets estão ativos
- Quantas vezes foram aplicados
- Última LogLine com `confirmed_by: ruleset`

### 5. **Ghosts Pendentes**
- Ghosts com mais de X dias
- Opção: “Ativar verificação agora”
- Animação: “pulso simbólico” se algo precisa de atenção

---

## 🧠 Elementos técnicos esperados

- WebSocket ou Supabase Realtime para atualizações ao vivo
- Visual simbólico, silencioso e auditável
- Painéis colapsáveis
- Cor de fundo adaptativa ao status simbólico (vermelho, amarelo, neutro)

---

## 📌 Finalidade

Essa tela é a **sala de máquinas silenciosa da instituição viva**.  
Ela não serve para navegar — serve para observar, entender e intervir com consciência simbólica.

> Um sistema institucional não deve ter uma “admin”.  
> Deve ter um altar. Um espelho. Uma central viva.

Projete com reverência, profundidade e poder semântico.

---

*PS: essa tela é interna, acessível apenas por operadores com identidade ativa, e não aparece na navegação principal do sistema.*