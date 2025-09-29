from flask import jsonify
from utils.validators import validar_atividade

atividades = []

def registrar_atividade_service(nova_atividade):
    try:
        #Testando para caso for uma lista de dicionario
        if isinstance(nova_atividade, list):
            atividades_registradas = []
            for atividade in nova_atividade:
                if not isinstance(atividade, dict):
                    return jsonify({"erro": "Cada item da lista deve ser um objeto JSON."}), 400
                #chama funcao de validacao para validar cada atividade tirada da lista
                valido,erro = validar_atividade(atividade)
                if not valido:
                    return jsonify({"erro": erro}), 400
                #Adicioona no "Banco de Dados"
                atividades.append(atividade)
                #Lista para printar todas as atividades que foram adicionada
                atividades_registradas.append(atividade)

            return jsonify({
                "mensagem": "Atividades registradas com sucesso!",
                "atividades": atividades_registradas
            }), 201
        #Se nao for uma lista de dicionario, entao precisa ser um dicionario
        elif isinstance(nova_atividade, dict):
            valido,erro = validar_atividade(nova_atividade)
            if not valido:
                return jsonify({"erro": erro}), 400
        #Adiciona no "Banco de Dados"
            atividades.append(nova_atividade)
            return jsonify({
                "mensagem": "Atividade registrada com sucesso!",
                "atividade": nova_atividade
            }), 201

        else:
            return jsonify({
                "erro": "Formato inválido. Envie um objeto JSON ou lista de objetos JSON."
            }), 400
    
    except Exception as e:
        return jsonify({
            "erro": "Erro ao processar a requisição.",
            "detalhes": str(e)
        }), 400
    
def listar_atividades_service():
    return jsonify(atividades), 200

def listar_por_funcional_service(funcional):
    try:
        atividades_funcionario = []
        #Para cada atividade listada no banco de dados
        for a in atividades:
            #Se o parametro funcional bater
            if isinstance(a, dict) and a.get("funcional") == funcional:
                #Entao pegamos os recursos que queremos da aquela funcional, e salvamos nessa lista para printar
                atividades_funcionario.append({
                    "codigoAtividade": a.get("codigoAtividade"),
                    "dataHora": a.get("dataHora"),
                    "descricaoAtividade": a.get("descricaoAtividade")
                })
        if not atividades_funcionario:
            return jsonify({
                "funcional": funcional,
                "atividades": [],
                "mensagem": "Nenhuma atividade encontrada para este funcional."
            }), 200

        return jsonify({
            "funcional": funcional,
            "atividades": atividades_funcionario
        }), 200

    except Exception as e:
        return jsonify({
            "erro": "Erro ao processar a requisição.",
            "detalhes": str(e)
        }), 400