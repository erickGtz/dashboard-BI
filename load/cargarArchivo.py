import pandas as pd
import sqlalchemy as sa
from backend.conexionBD import get_engine

# 1. Leer el CSV
df = pd.read_csv("Datasets/uber booking.csv")

# 2. Obtener el engine
engine = get_engine()

# 3. Subir el DataFrame a la base de datos como tabla nueva
df.to_sql("uber_booking", con=engine, if_exists="replace", index=False)

print("Datos subidos a la tabla 'uber_booking'")

# 4. Consultar algunos registros para verificar
with engine.connect() as conn:
    result = conn.execute(sa.text("SELECT * FROM uber_booking LIMIT 5"))
    for fila in result:
        print(fila)
