# 📊 Análise de Vendas e Faturamento em Python

Projeto desenvolvido para realizar uma análise exploratória de dados de vendas, focando em manipulação, agregação e visualização de dados.

## 🚀 Tecnologias Utilizadas
- **Python**
- **Pandas** (Tratamento e manipulação de dados)
- **Matplotlib** (Visualização gráfica)

## 📈 Etapas do Projeto
1. **Carregamento dos Dados:** Importação do arquivo CSV utilizando Pandas.
2. **Engenharia de Atributos:** Criação da coluna de *Faturamento Total* (`Quantidade` * `PrecoUnitario`).
3. **Agregação:** Agrupamento por categoria de produto (`groupby`) para somar o faturamento.
4. **Identificação de Métricas:** Localização do produto com maior volume de unidades vendidas.
5. **Visualização:** Geração de um gráfico de barras customizado para comparar o desempenho das categorias.

## 📊 Principais Resultados
- **Eletrônicos** lideraram o faturamento total.
- **Teclado** destacou-se como o produto com maior volume de unidades vendidas.
