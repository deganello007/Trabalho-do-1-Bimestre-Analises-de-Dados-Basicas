import pandas as pd
import numpy as np

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
max_correlation_value = correlation_matrix.abs().loc[max_correlation_pair[0], max_correlation_pair[1]]

# Imprime os resultados
print("Par de colunas com maior correlação:")
print(f"{max_correlation_pair[0]} e {max_correlation_pair[1]} - Correlação: {max_correlation_value}")
