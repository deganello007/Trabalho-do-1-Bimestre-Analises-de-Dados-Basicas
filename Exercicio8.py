import pandas as pd

# Lê o arquivo CSV e carrega os dados em um DataFrame
df = pd.read_csv("employee_data.csv")

# Remove as colunas "Gender" e "Age"
new_df = df.drop(columns=["Gender", "Age"])

# Imprime os 5 primeiros registros do novo DataFrame
print(new_df.head())
