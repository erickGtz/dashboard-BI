from flask import Flask, render_template
from backend.routers.api import api

app = Flask(__name__)
app.register_blueprint(api)

if __name__ == '__main__':
  app.run(debug=True, port=4000)