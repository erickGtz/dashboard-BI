from flask import Blueprint, render_template, request, jsonify
from ..plots.graficos_tipos_datos import grafico_tipos_datos, grafico_por_columna
from ..plots.graficos_nulos import grafico_valores_nulos
from ..plots.graficos_unicos import grafico_valores_unicos
from ..plots.info_general import mostrar_info_general
from ..load.cargar_excel import cargar_excel_a_bd
from ..DB_singleton import DatabaseSingleton

api = Blueprint("api", __name__)

@api.route("/", methods=['GET'])
def view():
    try:
        # Obtener datos actualizados
        db_singleton = DatabaseSingleton()
        num_observaciones, num_variables = mostrar_info_general()

        # Generar los gráficos utilizando los datos actuales
        numericas, categoricas, categoricas_muchas, booleanos, fechas = grafico_por_columna()

        grafico_valores_unicos()
        grafico_valores_nulos()
        grafico_tipos_datos()

        return render_template("index.html", 
                               observaciones=num_observaciones, 
                               variables=num_variables,
                               numericas=numericas,
                               categoricas=categoricas,
                               categoricas_muchas=categoricas_muchas,
                               booleanos=booleanos,
                               fechas=fechas)
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 500  # Error si no hay datos
    except Exception as e:
        return jsonify({"error": "Error al cargar los gráficos: " + str(e)}), 500



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

        # Recargar los datos en el Singleton para obtener la versión más reciente
        db_singleton = DatabaseSingleton()
        db_singleton.recargar_datos()  # Recargamos los datos después de la carga
        
        return jsonify({"message": "Archivo cargado y datos almacenados exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    



