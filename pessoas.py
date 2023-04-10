from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)

pessoas = [
    {"nome": "Paulo", "sexo": "M", "cabelo": "loiro"},
    {"nome": "Maria", "sexo": "F", "cabelo": "preto"},
    {"nome": "Fernanda", "sexo": "F", "cabelo": "ruivo"},
    {"nome": "José", "sexo": "M", "cabelo": "careca"}
]

def pessoa_ok(dic):
    return type(dic) == dict \
        and len(dic) == 3 \
        and "nome" in dic \
        and "sexo" in dic \
        and "cabelo" in dic \
        and type(dic["nome"]) == str \
        and dic["sexo"] in ["M", "F"] \
        and type(dic["cabelo"]) == str

@app.route("/pessoa", methods = ["POST"])
def cadastrar():
    pessoa = request.json # Passar um body na requisição
    if not pessoa_ok(pessoa):
        raise BadRequest
    pessoas.append(pessoa)
    return jsonify(pessoas)

@app.route("/pessoa/<int:id_pessoa>", methods = ["PUT"])
def atualizar(id_pessoa):
    pessoa = request.json
    if not pessoa_ok(pessoa):
        raise BadRequest
    if id_pessoa not in pessoas:
        raise NotFound
    pessoas[id_pessoa] = pessoa
    return pessoas

@app.route("/pessoa/<int:id_pessoa>", methods = ["GET"])
def selecionar(id_pessoa):
    if id_pessoa not in pessoas:
        raise NotFound
    return jsonify(pessoas[id_pessoa])

@app.route("/pessoa/<int:id_pessoa>", methods = ["DELETE"])
def deletar(id_pessoa):
    if id_pessoa in pessoas:
        del pessoas[id_pessoa]
    return pessoas

if __name__ == "__main__":
    app.run(host = "localhost", port = 5002)