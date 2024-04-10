import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lê o arquivo CSV e carrega os dados em um DataFrame
df = pd.read_csv("employee_data.csv")

# Exclui as colunas categóricas do DataFrame
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Calcula a matriz de correlação entre as colunas numéricas
correlation_matrix = numeric_df.corr()

# Filtra a matriz de correlação para excluir a diagonal principal (correlação de uma coluna com ela mesma)
correlation_matrix = correlation_matrix.mask(pd.DataFrame(np.eye(correlation_matrix.shape[0], dtype=bool), index=correlation_matrix.index, columns=correlation_matrix.columns))

# Encontra o par de colunas com a maior correlação absoluta
max_correlation_pair = correlation_matrix.abs().stack().idxmax()

# Extrai os nomes das colunas com a maior correlação
column1 = max_correlation_pair[0]
column2 = max_correlation_pair[1]

# Cria o gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(df[column1], df[column2], alpha=0.5)
plt.title(f'Gráfico de Dispersão entre {column1} e {column2}')
plt.xlabel(column1)
plt.ylabel(column2)
plt.grid(True)
plt.show()
