import matplotlib.pyplot as plt
import pandas as pd
from ..DB_singleton import DatabaseSingleton

def grafico_valores_nulos(output_path="static/images/valores_nulos.png"):
    db = DatabaseSingleton()
    df = db.obtener_datos()

    # Calcular nulos
    nulos = df.isnull().sum()
    total = df.shape[0]
    porcentaje_nulos = (nulos / total * 100).round(2)

    # Filtrar columnas con nulos
    nulos_filtrados = nulos.sort_values(ascending=True)  # Cambié de porcentaje_nulos a nulos
    nulos_absolutos = nulos[nulos_filtrados.index]

    # Si no hay nulos, no genera gráfico
    if nulos_filtrados.empty:
        print("No se encontraron valores nulos.")
        return

    # Gráfico
    plt.figure(figsize=(10, 6))
    bars = nulos_filtrados.plot(kind='barh', color='tomato')
    plt.xlabel('Número de valores nulos')
    plt.title('Número de valores nulos por columna')
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    # Etiquetas en cada barra
    for index, columna in enumerate(nulos_filtrados.index):
        cantidad = nulos_filtrados[columna]  # Cantidad de valores nulos
        porcentaje = porcentaje_nulos[columna]
        plt.text(cantidad + 500, index, f'{cantidad} valores ({porcentaje}%)', va='center', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
