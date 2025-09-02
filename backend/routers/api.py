from flask import Blueprint, render_template
from ..plots.graficos_tipos_datos import grafico_tipos_datos, grafico_por_columna
from ..plots.graficos_nulos import grafico_valores_nulos
from ..plots.graficos_unicos import grafico_valores_unicos
import os 

api = Blueprint("api", __name__)

@api.route("/")
def view():
    grafico_valores_nulos()
    grafico_tipos_datos()
    grafico_por_columna()

    # Obtener los archivos generados
    static_files = [f for f in os.listdir('static/images/graficos_por_columna/') if f.endswith('.png')]

    # Categorizar los gráficos
    numericas = [f for f in static_files if 'Boxplot' in f]
    categoricas = [f for f in static_files if 'Frecuencia' in f]
    categoricas_muchas = [f for f in static_files if 'Top N' in f]
    booleanos = [f for f in static_files if 'True/False' in f]
    fechas = [f for f in static_files if 'Diario' in f or 'Mensual' in f or 'Anual' in f]


    return render_template("index.html", 
                           numericas = numericas,
                           categoricas = categoricas, 
                           categoricas_muchas = categoricas_muchas,
                           booleanos = booleanos, 
                           fechas = fechas)



