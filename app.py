from flask import Flask
from flask_cors import CORS
from api.cliente_service import cliente

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(cliente, url_prefix='/api/cliente')

@app.route('/')
def hello():
    return "API Controle de Clientes"

@app.route('/teste')
def teste():
    return "<html><title>Teste</title><body><h1>Teste</h1></body></html>"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)