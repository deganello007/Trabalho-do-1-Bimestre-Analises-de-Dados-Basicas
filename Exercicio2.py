import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro

df = pd.read_csv("employee_data.csv")

colunas = ['Age', 'YearsAtCompany', 'YearsOfExperience', 'GrossSalary']

for coluna in colunas:
    stat, p = shapiro(df[coluna])
    
    plt.hist(df[coluna], bins=20, edgecolor='black')
    plt.title(f'Histograma da coluna {coluna}')
    plt.xlabel(coluna)
    plt.ylabel('Frequência')
    plt.show()

    print(f'Coluna: {coluna}')
    print(f'Estatística do teste de Shapiro-Wilk: {stat}')
    print(f'Valor p: {p}')

    alpha = 0.05
    if p > alpha:
        print("A distribuição parece normal (não podemos rejeitar H0)")
    else:
        print("A distribuição não parece normal (rejeitamos H0)")
    
    print('\n')
