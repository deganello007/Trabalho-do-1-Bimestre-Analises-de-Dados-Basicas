import pandas as pd

# Lê o arquivo CSV e carrega os dados em um DataFrame
df = pd.read_csv("employee_data.csv")

# Filtra os registros onde YearsOfExperience seja maior do que 10
filtered_df = df[df['YearsOfExperience'] > 10]

# Imprime os 5 últimos registros do novo DataFrame
print(filtered_df.tail())
