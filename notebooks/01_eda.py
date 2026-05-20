import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Cargar datos
df = pd.read_csv('../data/loan_train.csv')

print("✓ Datos cargados")
print("Filas y columnas:", df.shape)
print("\nPrimeras 5 filas:")
print(df.head())