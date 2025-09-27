from flask import Blueprint, request, jsonify
from services.atividades_service import registrar_atividade_service, listar_atividades_service, listar_por_funcional_service

atividades_bp = Blueprint("atividades", __name__)

@atividades_bp.route("", methods=["POST"])
def post_atividade():
    try:
        nova_atividade = request.get_json(force=True)
        return registrar_atividade_service(nova_atividade)
    except Exception as e:
        return jsonify({
            "erro": "Erro ao processar a requisição.",
            "detalhes": str(e)
        }), 400

@atividades_bp.route("", methods=["GET"])
def get_atividades():
    return listar_atividades_service()

@atividades_bp.route("/<funcional>", methods=["GET"])
def get_atividades_funcional(funcional):
    return listar_por_funcional_service(funcional)