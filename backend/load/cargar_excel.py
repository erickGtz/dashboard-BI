import pandas as pd
from backend.conexionBD import get_engine

def cargar_excel_a_bd(file):
  
    # Leer el archivo Excel (o CSV)
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # Obtener el engine de la base de datos
    engine = get_engine()

    # Subir los datos a la base de datos como tabla nueva
    df.to_sql("dataset", con=engine, if_exists="replace", index=False)
    
