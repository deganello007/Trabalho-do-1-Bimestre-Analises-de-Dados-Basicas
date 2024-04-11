import pandas as pd

df = pd.read_csv("employee_data.csv")

role_maior_frequencia = df['Role'].mode().iloc[0]
role_frequencia_maxima = df['Role'].value_counts()[role_maior_frequencia]

role_menor_frequencia = df['Role'].value_counts().idxmin()
role_frequencia_minima = df['Role'].value_counts()[role_menor_frequencia]

gender_maior_frequencia = df['Gender'].mode().iloc[0]
gender_frequencia_maxima = df['Gender'].value_counts()[gender_maior_frequencia]

gender_menor_frequencia = df['Gender'].value_counts().idxmin()
gender_frequencia_minima = df['Gender'].value_counts()[gender_menor_frequencia]

print("Valores de maior e menor frequência na coluna 'Role':")
print(f"Maior frequência: {role_maior_frequencia} - Frequência: {role_frequencia_maxima}")
print(f"Menor frequência: {role_menor_frequencia} - Frequência: {role_frequencia_minima}")
print("\n")

print("Valores de maior e menor frequência na coluna 'Gender':")
print(f"Maior frequência: {gender_maior_frequencia} - Frequência: {gender_frequencia_maxima}")
print(f"Menor frequência: {gender_menor_frequencia} - Frequência: {gender_frequencia_minima}")
