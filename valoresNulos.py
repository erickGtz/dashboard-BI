import pandas as pd
import matplotlib.pyplot as plt
from Database.conexionBD import get_engine

# Conexión y carga de datos
engine = get_engine()
df = pd.read_sql("SELECT * FROM uber_booking", con=engine)

# Cálculo de nulos
nulos = df.isnull().sum()
total = df.shape[0]
porcentajeNulos = (nulos / total * 100).round(2)

# Crear DataFrame resumen
tabla_nulos = pd.DataFrame({
    "Columna": df.columns,
    "Nulos": nulos.values,
    "Porcentaje (%)": porcentajeNulos.values
})

# Mostrar tabla completa
print("\n Tabla de valores nulos por columna:")
print(tabla_nulos)
tabla_nulos.to_csv("output/resumen_valores_nulos.csv", index=False)

# Filtrar columnas con nulos
nulos_filtrados = porcentajeNulos[porcentajeNulos > 0].sort_values(ascending=True)
nulos_absolutos = nulos[nulos_filtrados.index]

# Gráfico de barras horizontales
plt.figure(figsize=(10, 6))
bars = nulos_filtrados.plot(kind='barh', color='tomato')
plt.xlabel('Porcentaje de valores nulos (%)')
plt.title('Porcentaje de valores nulos por columna')
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Agregar etiquetas: porcentaje + cantidad
for index, columna in enumerate(nulos_filtrados.index):
    porcentaje = nulos_filtrados[columna]
    cantidad = nulos_absolutos[columna]
    plt.text(porcentaje + 0.5, index, f'{porcentaje}% ({cantidad})', va='center', fontsize=9)

plt.tight_layout()

plt.savefig("static/valores_nulos.png")  # debe ir ANTES de plt.show()
