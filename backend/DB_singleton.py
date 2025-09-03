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
        if self._df is None or self._df.empty:
            self._df = self._cargar_datos()
        return self._df
    
    def recargar_datos(self):
        """Recarga los datos del dataset después de un cambio (por ejemplo, después de cargar un nuevo Excel)."""
        self._df = None  # Limpiamos el cache
        return self.obtener_datos()

    @staticmethod
    def _cargar_datos():
        """Carga los datos de la base de datos."""
        engine = get_engine()
        query = "SELECT * FROM dataset"  # nombre de la tabla creada
        df = pd.read_sql(query, engine)
        
        # Verificamos si el DataFrame está vacío
        if df is None or df.empty:
            raise ValueError("No se han encontrado datos en la base de datos.")
        
        return df