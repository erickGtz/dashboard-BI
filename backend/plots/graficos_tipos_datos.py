import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
import numpy as np 
from ..conexionBD import get_engine
import os

def grafico_tipos_datos(output_path="static/images/tipos_datos.png"):
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM uber_booking", engine)

    tipo_datos = df.dtypes.value_counts()
    tipo_datos.plot(kind='bar', color='mediumseagreen')
    
    plt.title("Conteo de tipos de columnas")
    plt.xlabel("Tipo de dato")
    plt.ylabel("Cantidad")
    plt.tight_layout()

    plt.xticks(rotation=0)  #texto en horizontal

    for i, valor in enumerate(tipo_datos.values): # Agregar etiquetas con el conteo sobre cada barra
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=10)

    plt.savefig(output_path)
    plt.close()



def grafico_por_columna(output_dir="static/images/graficos_por_columna/"):
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM uber_booking", engine)

    # Inicializamos las listas para las categorías
    numericas = []
    categoricas = []
    categoricas_muchas = []
    booleanos = []
    fechas = []

    # Iterar sobre las columnas
    for columna in df.columns:
        serie = df[columna]
        tipo_dato = serie.dtypes

        output_path = os.path.join(output_dir, f"{columna}.png")

        # 1. Si es numérico
        if pd.api.types.is_numeric_dtype(serie):
            plt.figure(figsize=(8, 6))
            sns.boxplot(x=serie, color='lightblue')
            plt.title(f"Boxplot - {columna}")
            plt.tight_layout()
            plt.savefig(output_path)
            plt.close()
            numericas.append(f"{columna}.png")

        # 2. Si es categórico con pocas categorías
        elif tipo_dato == 'object' and serie.nunique() <= 7:
            plt.figure(figsize=(8, 6))
            serie.value_counts().plot(kind='bar', color='lightcoral')
            plt.title(f"Frecuencia de valores - {columna}")
            plt.xlabel(columna)
            plt.ylabel("Frecuencia")
            plt.tight_layout()
            plt.savefig(output_path)
            plt.close()
            categoricas.append(f"{columna}.png")

        # 3. Si es categórico con muchas categorías
        elif tipo_dato == 'object' and serie.nunique() > 7:
            top_n = serie.value_counts().nlargest(10)
            otros = serie.value_counts().iloc[10:].sum()
            top_n["Otros"] = otros

            plt.figure(figsize=(8, 6))
            top_n.plot(kind='bar', color='lightgreen')
            plt.title(f"Top N - {columna}")
            plt.xlabel(columna)
            plt.ylabel("Frecuencia")
            plt.tight_layout()
            plt.savefig(output_path)
            plt.close()
            categoricas_muchas.append(f"{columna}.png")

        # 4. Si es booleano
        elif tipo_dato == 'bool':
            plt.figure(figsize=(8, 6))
            serie.value_counts().plot(kind='bar', color=['blue', 'orange'])
            plt.title(f"Conteo de True/False - {columna}")
            plt.xlabel(columna)
            plt.ylabel("Frecuencia")
            plt.tight_layout()
            plt.savefig(output_path)
            plt.close()
            booleanos.append(f"{columna}.png")

        # 5. Si es fecha (datetime)
        elif pd.api.types.is_datetime64_any_dtype(serie):
            plt.figure(figsize=(8, 6))
            serie_resampled_day = serie.resample('D').count()  # Conteo diario
            serie_resampled_month = serie.resample('M').count()  # Conteo mensual
            serie_resampled_year = serie.resample('Y').count()  # Conteo anual

            plt.subplot(311)
            serie_resampled_day.plot(color='skyblue')
            plt.title(f"{columna} - Diario")
            plt.subplot(312)
            serie_resampled_month.plot(color='lightgreen')
            plt.title(f"{columna} - Mensual")
            plt.subplot(313)
            serie_resampled_year.plot(color='salmon')
            plt.title(f"{columna} - Anual")
            
            plt.tight_layout()
            plt.savefig(output_path)
            plt.close()
            fechas.append(f"{columna}.png")

    # Retornar las listas de gráficos generados
    return numericas, categoricas, categoricas_muchas, booleanos, fechas