import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee_data.csv")

colunas_numericas = ['Age', 'YearsAtCompany', 'YearsOfExperience', 'GrossSalary']

descritivas = df[colunas_numericas].describe()

print("Estatísticas descritivas:")
print(descritivas)
print("\n")

for coluna in colunas_numericas:
    plt.figure(figsize=(8, 6))
    plt.boxplot(df[coluna])
    plt.title(f'Boxplot da coluna {coluna}')
    plt.ylabel(coluna)
    plt.grid(True)
    plt.show()
