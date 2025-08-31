# connect_mysql_connector.py
import mysql.connector as mysql
import pandas as pd
from mysql.connector import errorcode

'''
cfg = dict(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="econautica",
)

try:
    cnx = mysql.connect(**cfg)
    cur = cnx.cursor(dictionary=True)
    cur.execute("SELECT * FROM usuarios;")
    for fila in cur.fetchall():
      print(fila["id"], fila["nombre"])
    cur.close()
    cnx.close()
except mysql.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuario o contraseña incorrectos")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos no existe")
    else:
        print("Error:", e)

'''

# Carga tu archivo CSV
df = pd.read_csv('Datasets/uber booking.csv')

# Verifica que se cargó bien
print(df.head())
print(df.columns)