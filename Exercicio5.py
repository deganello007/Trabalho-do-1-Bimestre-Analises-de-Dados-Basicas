import pandas as pd
import numpy as np

df = pd.read_csv("employee_data.csv")

numeric_df = df.select_dtypes(include=['int64', 'float64'])

correlation_matrix = numeric_df.corr()

correlation_matrix = correlation_matrix.mask(pd.DataFrame(np.eye(correlation_matrix.shape[0], dtype=bool), index=correlation_matrix.index, columns=correlation_matrix.columns))

max_correlation_pair = correlation_matrix.abs().stack().idxmax()
max_correlation_value = correlation_matrix.abs().loc[max_correlation_pair[0], max_correlation_pair[1]]

print("Par de colunas com maior correlação:")
print(f"{max_correlation_pair[0]} e {max_correlation_pair[1]} - Correlação: {max_correlation_value}")
