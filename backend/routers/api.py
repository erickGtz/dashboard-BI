from flask import Blueprint, render_template
from ..plots.graficos import grafico_tipos_datos

api = Blueprint("api", __name__)

@api.route("/")
def home():
    grafico_tipos_datos()
    return render_template("index.html")
