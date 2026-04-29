---
# Sistema de Reservatório
---
Mudança do nível do reservatório em tempo real, e display de mensagens com cores usando a biblioteca colorama

---
O programa simula o comportamento do nível do reservatório de uma represa, apresentando períodos de seca, chuva e clima estável, além de mostrar mensagens com respectivas cores para cada nível da represa.

| Nível         | Faixa     | Cor        |
|---------------|-----------|------------|
| Muito Alto    | > 85%     | 🔵 Azul    |
| Alto          | 71% – 85% | 🩵 Ciano   |
| Médio         | 51% – 70% | 🟢 Verde   |
| Baixo         | 31% – 50% | 🟡 Amarelo |
| Muito Baixo   | ≤ 30%     | 🔴 Vermelho|

---
Pré-requisitos:

Biblioteca *colorama* instalada