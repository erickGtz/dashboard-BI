import pandas as pd
from ..conexionBD import get_engine

def mostrar_info_general():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM uber_booking", engine)

    # Obtener el número de observaciones (filas) y variables (columnas)
    num_observaciones = df.shape[0]  # Número de filas
    num_variables = df.shape[1]  # Número de columnas

    return num_observaciones, num_variables  # Retornar los valores si es necesario
