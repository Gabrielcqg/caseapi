from flask import jsonify
from utils.validators import validar_atividade
from repositories.atividades_repository import carregar_atividades, salvar_atividades

atividades = []

def registrar_atividade_service(nova_atividade):
    try:
        # Carrega dados existentes do "banco" (JSON local)
        atividades = carregar_atividades()

        # Caso seja uma lista de dicionários
        if isinstance(nova_atividade, list):
            atividades_registradas = []
            for atividade in nova_atividade:
                if not isinstance(atividade, dict):
                    return jsonify({"erro": "Cada item da lista deve ser um objeto JSON."}), 400

                # Chama função de validação para cada atividade
                valido, erro = validar_atividade(atividade)
                if not valido:
                    return jsonify({"erro": erro}), 400

                # Adiciona no "banco de dados" (lista carregada do JSON)
                atividades.append(atividade)
                atividades_registradas.append(atividade)

            # Salva todas as novas atividades no JSON
            salvar_atividades(atividades)

            return jsonify({
                "mensagem": "Atividades registradas com sucesso!",
                "atividades": atividades_registradas
            }), 201

        # Caso seja apenas um dicionário
        elif isinstance(nova_atividade, dict):
            valido, erro = validar_atividade(nova_atividade)
            if not valido:
                return jsonify({"erro": erro}), 400

            atividades.append(nova_atividade)
            salvar_atividades(atividades)

            return jsonify({
                "mensagem": "Atividade registrada com sucesso!",
                "atividade": nova_atividade
            }), 201

        # Caso não seja lista nem dicionário
        else:
            return jsonify({
                "erro": "Formato inválido. Envie um objeto JSON ou lista de objetos JSON."
            }), 400

    except Exception as e:
        return jsonify({
            "erro": "Erro ao processar a requisição.",
            "detalhes": str(e)
        }), 500

def listar_atividades_service():
    try:
        atividades = carregar_atividades()
        return jsonify(atividades), 200
    except Exception as e:
        return jsonify({"erro": "Erro ao listar atividades.", "detalhes": str(e)}), 500

def listar_por_funcional_service(funcional):
    try:
        atividades = carregar_atividades()  # agora buscamos do JSON
        atividades_funcionario = []

        # Para cada atividade listada no "banco de dados" (JSON)
        for a in atividades:
            # Se o parâmetro funcional bater
            if isinstance(a, dict) and a.get("funcional") == funcional:
                # Pegamos apenas os campos desejados
                atividades_funcionario.append({
                    "codigoAtividade": a.get("codigoAtividade"),
                    "dataHora": a.get("dataHora"),
                    "descricaoAtividade": a.get("descricaoAtividade")
                })

        # Se não achou nada, retorna mensagem
        if not atividades_funcionario:
            return jsonify({
                "funcional": funcional,
                "atividades": [],
                "mensagem": "Nenhuma atividade encontrada para este funcional."
            }), 200

        # Se achou, retorna lista filtrada
        return jsonify({
            "funcional": funcional,
            "atividades": atividades_funcionario
        }), 200

    except Exception as e:
        return jsonify({
            "erro": "Erro ao processar a requisição.",
            "detalhes": str(e)
        }), 500
