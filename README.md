# Smart Energy Colony

## 1. Descrição
O Smart Energy Colony é um sistema desenvolvido em Python para representar
o gerenciamento inteligente de energia de uma colônia. O programa organiza
dados, aplica regras de decisão, estima a geração de energia por regressão
linear simples e compara geração, consumo e reserva.

## 2. Objetivos
- Organizar informações de energia, clima e sistemas da colônia.
- Tomar decisões automáticas com regras lógicas.
- Prever a geração de energia a partir da velocidade do vento.
- Analisar o equilíbrio entre geração e consumo.

## 3. Tecnologias
- Python 3
- Bibliotecas padrão do Python (nenhuma instalação externa necessária)

## 4. Como executar
1. Instale o Python 3.
2. Abra a pasta do projeto no Visual Studio Code.
3. Abra o terminal integrado.
4. Execute:

```bash
python main.py
```

No Windows, também pode ser necessário usar:

```bash
py main.py
```

## 5. Organização dos dados
Os dados são organizados em dicionários e listas.
O dicionário principal guarda energia, clima, sistemas e históricos.
Os sistemas são agrupados hierarquicamente em energético, essenciais e
não essenciais. Essa organização facilita o acesso e a atualização dos dados.

## 6. Regras de decisão
- O suporte à vida permanece ligado por ser essencial.
- Se o consumo for maior que a geração, o sistema emite um alerta e recomenda
  economia, desligando sistemas não essenciais.
- Se a geração for maior que o consumo, o sistema recomenda armazenar o excedente.
- Se a geração for menor que 50 unidades, o sistema recomenda reduzir o consumo.
- Se a reserva for zero, o sistema emite um alerta de reserva indisponível.

## 7. Modelo de previsão
O sistema utiliza regressão linear simples, representada por:

`y = a * x + b`

Em que:
- `x` representa a velocidade do vento;
- `y` representa a geração estimada de energia;
- `a` é a inclinação da reta;
- `b` é o ponto em que a reta cruza o eixo y.

Dados de exemplo:
- Vento: [8, 10, 12]
- Energia: [20, 25, 30]

Com vento igual a 11, a previsão é de aproximadamente 27,5 unidades.
O enunciado apresenta aproximadamente 27 como referência.

## 8. Exemplo de análise
Com geração igual a 40 e consumo igual a 70, o sistema identifica que o
consumo está maior que a geração, apresenta um alerta e recomenda reduzir
o consumo. Os sistemas não essenciais são desligados na simulação, enquanto
o suporte à vida permanece ligado.

Com geração igual a 80 e consumo igual a 30, o sistema identifica um
excedente de 50 unidades e recomenda armazenar essa energia.

## 9. Como o sistema ajuda a colônia
O sistema transforma dados em recomendações objetivas. Isso ajuda a
identificar falta ou excedente de energia, priorizar sistemas essenciais
e planejar a geração futura com base no vento.

## 10. Limitações
Este projeto é uma simulação acadêmica. Os dados são informados pelo usuário
ou definidos como exemplos no código. A previsão utiliza poucos pontos
históricos e uma relação linear simplificada; portanto, não substitui um
sistema real de gestão energética.

## 11. Estrutura do projeto
- `main.py`: implementação do sistema.
- `README.md`: documentação.
- `requirements.txt`: dependências do projeto.
