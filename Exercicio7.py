import pandas as pd

df = pd.read_csv("employee_data.csv")

filtered_df = df[df['YearsOfExperience'] > 10]

print(filtered_df.tail())
