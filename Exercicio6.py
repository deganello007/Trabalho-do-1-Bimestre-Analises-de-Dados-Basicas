import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("employee_data.csv")


plt.figure(figsize=(8, 6))
plt.scatter(df["YearsOfExperience"], df["GrossSalary"], alpha=0.5)
plt.title(f'Gráfico de Dispersão entre YearsOfExperience e GrossSalary')
plt.xlabel("YearsOfExperience")
plt.ylabel("GrossSalary")
plt.grid(True)
plt.show()
