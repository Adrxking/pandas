import pandas as pd

df = pd.read_csv('pandas/data.csv')

# Eliminar registros con celdas vacías
df2 = df.dropna()

# Reemplazar valores vacíos
mean = df['Calories'].mean()
df3 = df['Calories'].fillna(mean)

# Formatos inadecuados
df['Date'] = pd.to_datetime(df['Date'])
# df.dropna(subset=['Date'], inplace=True)z

print(df)