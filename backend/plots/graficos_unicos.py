import matplotlib.pyplot as plt
import pandas as pd
from ..conexionBD import get_engine

def grafico_valores_unicos(output_path="static/images/valores_unicos.png"):
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM uber_booking", engine)

    valores_unicos = df.nunique()  # Cuenta los valores únicos por columna
    total = df.shape[0]  # Total de registros

    porcentaje_unicos = (valores_unicos / total * 100).round(2)

    valores_unicos_filtrados = porcentaje_unicos[porcentaje_unicos > 0].sort_values(ascending=True)

    if valores_unicos_filtrados.empty:
        print("No se encontraron valores únicos.")
        return

    plt.figure(figsize=(10, 6))
    bars = valores_unicos_filtrados.plot(kind='barh', color='skyblue')
    plt.xlabel('Porcentaje de valores únicos (%)')
    plt.title('Porcentaje de valores únicos por columna')
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    for index, columna in enumerate(valores_unicos_filtrados.index):
        porcentaje = valores_unicos_filtrados[columna]
        cantidad = df[columna].nunique()  # Cantidad de valores únicos
        plt.text(porcentaje + 0.5, index, f'{porcentaje}% ({cantidad} valores)', va='center', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
