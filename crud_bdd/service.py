from datetime import datetime
from repository import DisciplinaRepository

repository = DisciplinaRepository()


def validar_disciplina(dados):
    erros = []

    if dados is None:
        return ["O corpo da requisição não pode estar vazio."]

    if "titulo" not in dados or not str(dados["titulo"]).strip():
        erros.append("O campo 'titulo' é obrigatório.")

    if "data_inicio" not in dados or not str(dados["data_inicio"]).strip():
        erros.append("O campo 'data_inicio' é obrigatório.")

    if "data_termino" not in dados or not str(dados["data_termino"]).strip():
        erros.append("O campo 'data_termino' é obrigatório.")

    if "numero_vagas" not in dados:
        erros.append("O campo 'numero_vagas' é obrigatório.")
    else:
        if not isinstance(dados["numero_vagas"], int) or dados["numero_vagas"] <= 0:
            erros.append("O campo 'numero_vagas' deve ser um inteiro maior que zero.")

    if "eh_verao" not in dados:
        erros.append("O campo 'eh_verao' é obrigatório.")
    else:
        if not isinstance(dados["eh_verao"], bool):
            erros.append("O campo 'eh_verao' deve ser booleano.")

    if "data_inicio" in dados and "data_termino" in dados:
        try:
            inicio = datetime.strptime(dados["data_inicio"], "%Y-%m-%d")
            termino = datetime.strptime(dados["data_termino"], "%Y-%m-%d")
            if termino < inicio:
                erros.append("A data de término não pode ser anterior à data de início.")
        except ValueError:
            erros.append("As datas devem estar no formato YYYY-MM-DD.")

    return erros


def listar_disciplinas():
    return [disciplina.to_dict() for disciplina in repository.listar_todas()]


def buscar_disciplina_por_id(disciplina_id):
    disciplina = repository.buscar_por_id(disciplina_id)
    if not disciplina:
        return None
    return disciplina.to_dict()


def criar_disciplina(dados):
    erros = validar_disciplina(dados)
    if erros:
        return {"erros": erros}, 400

    disciplina = repository.criar(
        titulo=dados["titulo"],
        data_inicio=dados["data_inicio"],
        data_termino=dados["data_termino"],
        numero_vagas=dados["numero_vagas"],
        eh_verao=dados["eh_verao"]
    )
    return disciplina.to_dict(), 201


def atualizar_disciplina(disciplina_id, dados):
    disciplina_existente = repository.buscar_por_id(disciplina_id)
    if not disciplina_existente:
        return {"erro": "Disciplina não encontrada."}, 404

    erros = validar_disciplina(dados)
    if erros:
        return {"erros": erros}, 400

    disciplina_atualizada = repository.atualizar(disciplina_id, dados)
    return disciplina_atualizada.to_dict(), 200


def remover_disciplina(disciplina_id):
    removido = repository.remover(disciplina_id)
    if not removido:
        return {"erro": "Disciplina não encontrada."}, 404

    return "", 204