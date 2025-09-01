from flask import Blueprint, render_template
from ..plots.graficos_tipos_datos import grafico_tipos_datos
from ..plots.graficos_nulos import grafico_valores_nulos

api = Blueprint("api", __name__)

@api.route("/")
def nulos_view():
    grafico_valores_nulos()
    return render_template("index.html")

@api.route("/")
def tipos_datos_view():
    grafico_tipos_datos()
    return render_template("index.html")

