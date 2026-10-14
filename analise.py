import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados 
df = pd.read_csv("dados_vendas.csv")

print("--- PRIMEIRAS LINHAS DE DADOS ---")
print(df.head(), "\n")

# 2. Tratamento e Transformaçaõ (Criar coluna de Faturamento Total)
df['Faturamento_Total'] = df['Quantidade'] * df['PrecoUnitario']

# 3. Análise Agregada: Faturamento por Categoria
faturamento_categoria = df.groupby('Categoria')['Faturamento_Total'].sum()

print("--- FATURAMENTO POR CATEGORIA ---")
print(faturamento_categoria, "\n")

# 4. Identificar o produto mais vendido por quantidade
produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()
print(f"Produto com maior volume de unidades vendidas: {produto_mais_vendido}\n")

# 5. Visualização Gráfica
faturamento_categoria.plot(kind='bar', color=['#3498db', '#2ecc71'])
plt.title('Faturamento Total por Categoria de Produto')
plt.xlabel('Categoria')
plt.ylabel('Faturamento Total (R$)')
plt.xticks(rotation=0)
plt.tight_layout()

# Exibir o gráfico gerado
plt.show()