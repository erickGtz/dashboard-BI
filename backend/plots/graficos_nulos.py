import matplotlib.pyplot as plt
import pandas as pd
from ..conexionBD import get_engine

def grafico_valores_nulos(output_path="static/images/valores_nulos.png"):
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM uber_booking", engine)

  # Calcular nulos
    nulos = df.isnull().sum()
    total = df.shape[0]
    porcentaje_nulos = (nulos / total * 100).round(2)

    # Filtrar columnas con nulos
    nulos_filtrados = porcentaje_nulos[porcentaje_nulos > 0].sort_values(ascending=True)
    nulos_absolutos = nulos[nulos_filtrados.index]

    # Si no hay nulos, no genera gráfico
    if nulos_filtrados.empty:
      print("No se encontraron valores nulos.")
      return

    # Gráfico
    plt.figure(figsize=(10, 6))
    bars = nulos_filtrados.plot(kind='barh', color='tomato')
    plt.xlabel('Porcentaje de valores nulos (%)')
    plt.title('Porcentaje de valores nulos por columna')
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    # Etiquetas en cada barra
    for index, columna in enumerate(nulos_filtrados.index):
      porcentaje = nulos_filtrados[columna]
      cantidad = nulos_absolutos[columna]
      plt.text(porcentaje + 0.5, index, f'{porcentaje}% ({cantidad} valores)', va='center', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
