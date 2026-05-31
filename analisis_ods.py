import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("datos_inegi.csv")

# Mostrar información general
print("Primeras filas:")
print(df.head())

print("\nResumen estadístico:")
print(df.describe())

# Eliminar valores faltantes
df = df.dropna()

# Agrupar información por entidad
resumen = df.groupby("Entidad")["Valor"].mean().reset_index()

# Mostrar resultados
print("\nPromedio por entidad:")
print(resumen)

# Crear visualización
fig = px.bar(
    resumen,
    x="Entidad",
    y="Valor",
    title="Indicador promedio por entidad federativa",
    labels={"Valor": "Valor del indicador"}
)

fig.show()
