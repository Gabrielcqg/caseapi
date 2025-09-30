from flask import Blueprint, request
from services.atividades_service import (
    registrar_atividade_service,
    listar_atividades_service,
    listar_por_funcional_service
)
atividades_bp = Blueprint("atividades", __name__)

@atividades_bp.route("", methods=["POST"])
def post_atividade():
    nova_atividade = request.get_json(force=True) 
    return registrar_atividade_service(nova_atividade)

@atividades_bp.route("", methods=["GET"])
def get_atividades():
    return listar_atividades_service()

@atividades_bp.route("/<funcional>", methods=["GET"])
def get_atividades_funcional(funcional):
    return listar_por_funcional_service(funcional)
