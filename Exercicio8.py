import pandas as pd

df = pd.read_csv("employee_data.csv")

new_df = df.drop(columns=["Gender", "Age"])

print(new_df.head())
