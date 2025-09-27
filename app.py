"""
Objetivo : Desenvolver uma API RESTful simples que permita o registro e a 
consulta de atividades físicas realizadas por funcionários.

3 funcoes:
(Criar / Registrar atividade (POST))
(Listar Atividades(GET))
(Listar atividades por Funcional(GET)com parametro)

"""

from flask import Flask
from routes.atividades_routes import atividades_bp

def create_app():
    app = Flask(__name__)

    # Registro dos blueprints
    app.register_blueprint(atividades_bp, url_prefix="/atividades")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

