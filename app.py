from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("output/resumen_valores_nulos.csv")  # o cargar desde SQL
    tabla_html = df.to_html(classes="table", index=False)
    return render_template("dashboard.html", tabla=tabla_html)

if __name__ == "__main__":
    app.run(debug=True)
