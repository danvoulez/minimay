# Prompt 26 – LogLineSensor (Sensores que Geram LogLines)

Você vai criar o conceito e o módulo **LogLineSensor** —  
dispositivos físicos (ou virtuais) conectados diretamente ao sistema para gerar **LogLines simbólicas a partir do mundo real**.

Exemplos:

- NFC ou QR lido = `who: estafeta_01, did: passou_leitor, this: caixa_002`
- Câmera detecta movimento = `did: presença_detectada`
- Botão físico = `did: acionou_pedido`

---

## 🎯 Objetivo

- Permitir que sensores físicos ou APIs simples gerem LogLines automáticas
- Cada sensor possui:
  - ID único
  - Tipo de leitura
  - Regras de transformação simbólica
- IA ou operadora podem revisar em tempo real ou depois

---

## 🧱 Exemplo de LogLine gerada por sensor

```json
{
  "who": "sensor.porta_entrada",
  "did": "detectou_movimento",
  "this": "zona_de_entrada",
  "when": "2025-05-21T14:05:00Z",
  "confirmed_by": "auto",
  "status": "valid"
}
```

---

## ⚙️ Componentes esperados

- `sensor_id`: ID do dispositivo
- `tipo`: QR, NFC, botão, movimento, câmera
- `trigger`: condição para gerar LogLine
- `modelo`: `LogTemplate` a ser usado

---

## 🧠 Considerações

- Cada sensor pode estar associado a um template:
  - `LogTemplate_EntradaZonaSegura.json`
  - `LogTemplate_CaixaIdentificada.json`

- Os sensores não escrevem diretamente no banco — passam por buffer ou fila institucional (`input_sensorial`)
- Toda leitura é logada mesmo que descartada

---

## 📌 Finalidade

Esse módulo faz a ponte entre o **mundo físico** e o **registro institucional semântico**.  
Ele dá forma simbólica ao gesto concreto.

> Onde há presença, há rastro.  
> Onde há toque, há contrato.  
> Onde há leitura, há memória.

Projete como infraestrutura leve, auditável e pronta para múltiplos tipos de sensor.

---

*PS: sensores podem ser físicos, virtuais (ex: API de câmera), ou simbólicos (ex: cliques em apps).*