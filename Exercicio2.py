import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro

# Carrega os dados do arquivo CSV para um DataFrame
df = pd.read_csv("employee_data.csv")

# Lista das colunas a serem analisadas
colunas = ['Age', 'YearsAtCompany', 'YearsOfExperience', 'GrossSalary']

# Loop sobre cada coluna
for coluna in colunas:
    # Calcula o teste de Shapiro-Wilk
    stat, p = shapiro(df[coluna])
    
    # Plota o histograma
    plt.hist(df[coluna], bins=20, edgecolor='black')
    plt.title(f'Histograma da coluna {coluna}')
    plt.xlabel(coluna)
    plt.ylabel('Frequência')
    plt.show()
    
    # Imprime o resultado do teste de Shapiro-Wilk
    print(f'Coluna: {coluna}')
    print(f'Estatística do teste de Shapiro-Wilk: {stat}')
    print(f'Valor p: {p}')
    
    # Verifica se a distribuição é normal com base no valor p
    alpha = 0.05
    if p > alpha:
        print("A distribuição parece normal (não podemos rejeitar H0)")
    else:
        print("A distribuição não parece normal (rejeitamos H0)")
    
    print('\n')
