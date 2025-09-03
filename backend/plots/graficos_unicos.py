import matplotlib.pyplot as plt
import pandas as pd
from ..DB_singleton import DatabaseSingleton

def grafico_valores_unicos(output_path="static/images/valores_unicos.png"):
    db = DatabaseSingleton()
    df = db.obtener_datos()

    valores_unicos = df.nunique()  # Cuenta los valores únicos por columna
    total = df.shape[0]  # Total de registros

    porcentaje_unicos = (valores_unicos / total * 100).round(2)

    valores_unicos_filtrados = valores_unicos.sort_values(ascending=True)

    if valores_unicos_filtrados.empty:
        print("No se encontraron valores únicos.")
        return

    plt.figure(figsize=(10, 6))
    bars = valores_unicos_filtrados.plot(kind='barh', color='skyblue')
    plt.xlabel('Número de valores únicos')
    plt.title('Número de valores únicos por columna')
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    # Etiquetas en cada barra
    for index, columna in enumerate(valores_unicos_filtrados.index):
        cantidad = valores_unicos_filtrados[columna]  # Cantidad de valores únicos
        porcentaje = porcentaje_unicos[columna]
        plt.text(cantidad + 0.5, index, f'{cantidad} valores ({porcentaje}%)', va='center', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
