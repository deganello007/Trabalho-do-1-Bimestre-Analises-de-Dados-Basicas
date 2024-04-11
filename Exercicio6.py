import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("employee_data.csv")

numeric_df = df.select_dtypes(include=['int64', 'float64'])

correlation_matrix = numeric_df.corr()

correlation_matrix = correlation_matrix.mask(pd.DataFrame(np.eye(correlation_matrix.shape[0], dtype=bool), index=correlation_matrix.index, columns=correlation_matrix.columns))

max_correlation_pair = correlation_matrix.abs().stack().idxmax()

column1 = max_correlation_pair[0]
column2 = max_correlation_pair[1]

plt.figure(figsize=(8, 6))
plt.scatter(df[column1], df[column2], alpha=0.5)
plt.title(f'Gráfico de Dispersão entre {column1} e {column2}')
plt.xlabel(column1)
plt.ylabel(column2)
plt.grid(True)
plt.show()
