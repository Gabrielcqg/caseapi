from datetime import datetime

def validar_atividade(nova_atividade):

    # Validacao dos campos
    campos_obrigatorios = ["funcional", "dataHora", "codigoAtividade", "descricaoAtividade"]
    for campo in campos_obrigatorios:
        if campo not in nova_atividade:
            return False, f"Campo obrigatório '{campo}' ausente."

    # Validacao da funcional
    if not nova_atividade["funcional"].isdigit():
        return False, "O campo 'funcional' deve conter apenas números."

    if len(nova_atividade["funcional"]) != 6:
        return False, "O campo 'funcional' deve ter exatamente 6 dígitos."

    # Validacao da data
    try:
        datetime.strptime(nova_atividade["dataHora"], "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return False, "O campo 'dataHora' deve estar no formato YYYY-MM-DDTHH:MM:SS"

    # Validacao do código de atividade
    if not isinstance(nova_atividade["codigoAtividade"], str) or len(nova_atividade["codigoAtividade"]) != 3 or not nova_atividade["codigoAtividade"].isalpha():
        return False, "O campo 'codigoAtividade' deve ser uma string de exatamente 3 letras (ex: RUN)."

    # Validacaos da descrição
    if "descricaoAtividade" in nova_atividade:
        if not isinstance(nova_atividade["descricaoAtividade"], str):
            return False, "O campo 'descricaoAtividade' deve ser texto."
        if len(nova_atividade["descricaoAtividade"]) > 200:
            return False, "O campo 'descricaoAtividade' deve ter no máximo 200 caracteres."

    return True, None