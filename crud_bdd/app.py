from flask import Flask, request, jsonify
from service import (
    listar_disciplinas,
    buscar_disciplina_por_id,
    criar_disciplina,
    atualizar_disciplina,
    remover_disciplina
)

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"mensagem": "API de disciplinas funcionando"}), 200


@app.route("/disciplinas", methods=["POST"])
def criar():
    dados = request.get_json()
    resposta, status = criar_disciplina(dados)
    if resposta == "":
        return "", status
    return jsonify(resposta), status


@app.route("/disciplinas", methods=["GET"])
def listar():
    return jsonify(listar_disciplinas()), 200


@app.route("/disciplinas/<int:disciplina_id>", methods=["GET"])
def buscar(disciplina_id):
    disciplina = buscar_disciplina_por_id(disciplina_id)
    if not disciplina:
        return jsonify({"erro": "Disciplina não encontrada."}), 404
    return jsonify(disciplina), 200


@app.route("/disciplinas/<int:disciplina_id>", methods=["PUT"])
def atualizar(disciplina_id):
    dados = request.get_json()
    resposta, status = atualizar_disciplina(disciplina_id, dados)
    if resposta == "":
        return "", status
    return jsonify(resposta), status


@app.route("/disciplinas/<int:disciplina_id>", methods=["DELETE"])
def remover(disciplina_id):
    resposta, status = remover_disciplina(disciplina_id)
    if resposta == "":
        return "", status
    return jsonify(resposta), status


if __name__ == "__main__":
    app.run(debug=True)