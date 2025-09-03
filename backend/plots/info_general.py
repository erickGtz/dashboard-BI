import pandas as pd
from ..DB_singleton import DatabaseSingleton

def mostrar_info_general():
    db = DatabaseSingleton()
    df = db.obtener_datos()

    # Obtener el número de observaciones (filas) y variables (columnas)
    num_observaciones = df.shape[0]  # Número de filas
    num_variables = df.shape[1]  # Número de columnas

    return num_observaciones, num_variables  # Retornar los valores si es necesario
