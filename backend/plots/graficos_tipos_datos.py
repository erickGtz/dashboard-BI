import matplotlib.pyplot as plt
import pandas as pd
from ..conexionBD import get_engine

def grafico_tipos_datos(output_path="static/images/tipos_datos.png"):
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM uber_booking", engine)

    tipo_datos = df.dtypes.value_counts()
    tipo_datos.plot(kind='bar', color='mediumseagreen')
    
    plt.title("Conteo de tipos de columnas")
    plt.xlabel("Tipo de dato")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
