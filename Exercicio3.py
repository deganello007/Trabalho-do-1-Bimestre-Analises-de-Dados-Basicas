import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados do arquivo CSV para um DataFrame
df = pd.read_csv("employee_data.csv")

# Lista das colunas numéricas
colunas_numericas = ['Age', 'YearsAtCompany', 'YearsOfExperience', 'GrossSalary']

# Calcula as estatísticas descritivas para cada coluna numérica
descritivas = df[colunas_numericas].describe()

# Imprime as estatísticas descritivas
print("Estatísticas descritivas:")
print(descritivas)
print("\n")

# Cria os gráficos de caixa (boxplot) para cada coluna numérica
for coluna in colunas_numericas:
    plt.figure(figsize=(8, 6))
    plt.boxplot(df[coluna])
    plt.title(f'Boxplot da coluna {coluna}')
    plt.ylabel(coluna)
    plt.grid(True)
    plt.show()
