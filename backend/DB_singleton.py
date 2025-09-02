import pandas as pd
from .conexionBD import get_engine

class DatabaseSingleton:
    _instance = None
    _df = None

    def __new__(cls):
        """Implementa el patrón Singleton: asegura que solo haya una instancia."""
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
        return cls._instance

    def obtener_datos(self):
        """Obtiene los datos de la base de datos, pero solo una vez."""
        # Si los datos no han sido cargados previamente
        if self._df is None:
            engine = get_engine()  # Conectar a la base de datos
            # Consulta real a la tabla 'uber_booking'
            query = """
                SELECT * 
                FROM uber_booking
            """
            self._df = pd.read_sql(query, engine)  # Ejecuta el SELECT y carga los datos
        return self._df  # Retorna el DataFrame cargado
