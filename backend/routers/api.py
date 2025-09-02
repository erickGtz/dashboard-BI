from flask import Blueprint, render_template, request, jsonify
from ..plots.graficos_tipos_datos import grafico_tipos_datos, grafico_por_columna
from ..plots.graficos_nulos import grafico_valores_nulos
from ..load.cargar_excel import cargar_excel_a_bd
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


# Ruta para cargar el archivo Excel
@api.route('/upload', methods=['POST'])
def upload_file():
    # Verificar si el archivo está presente en la solicitud
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file part"}), 400

    # Verificar si se ha cargado un archivo válido
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Llamamos a la función de carga, que ya maneja la lógica completa
        cargar_excel_a_bd(file)
        
        return jsonify({"message": "Archivo cargado y datos almacenados exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    



