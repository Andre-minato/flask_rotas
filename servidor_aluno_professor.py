from flask import Flask, jsonify, request

app = Flask(__name__)

database = {
    'ALUNO' : [
                {"id": 1, "nome": "Andreia"},
                {"id": 2, "nome": "Arthur"},
                {"id": 3, "nome": "Pedro"}],
    'PROFESSOR': [
                    {"id": 1, "nome": "Professor1"},
                    {"id": 2, "nome": "Professor2"},
                    {"id": 3, "nome": "Professor3"}]

}
#Retorna String ("Vamos aprender a integrar Requests e Flask!")
@app.route("/")
def start():
    return "Vamos aprender a integrar Requests e Flask!"

#Retorna os alunos
@app.route("/alunos")
def getAlunos():
    return jsonify(database['ALUNO'])

#Retorna os professores
@app.route("/professores")
def getProfessores():
    return jsonify(database['PROFESSOR'])

#Retorna os alunos e professores
@app.route("/show_all")
def getAll():
    return jsonify(database)

#Adicionar um novo aluno metodo POST
@app.route("/adicionando_alunos", methods=['POST'])
def inserir_aluno():
    novo_aluno = request.json #Metodo pede um body na requisição
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])

#Atualiza aluno
@app.route("/alunos/<int:id_aluno>", methods=['PUT'])
def atualizar(id_aluno):
    atualiza_aluno = request.get_json()#Metodo pede um body na requisição
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            database['ALUNO'].remove(aluno)
            database['ALUNO'].append(atualiza_aluno)
            return jsonify(database['ALUNO'])
    return 'Aluno não encontrado', 404

#Excluir um aluno
@app.route("/alunos/<int:id_aluno>", methods=['DELETE'])
def excluir_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            database['ALUNO'].remove(aluno)
            return jsonify(database['ALUNO'])
    return 'Aluno não encontrado', 404

#Pesquisar aluno pelo id
@app.route("/alunos/<int:id_aluno>", methods=['Get'])
def localizar_aluno_id(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return 'Aluno não encontrado', 404

#Pesquisar aluno pelo nome
@app.route("/alunos/<nome_aluno>", methods=["GET"])
def localizar_aluno_nome(nome_aluno):
    for aluno in database['ALUNO']:
        if aluno['nome'] == nome_aluno:
            return jsonify(aluno)
    return 'Aluno não encontrado', 404

#Apagar dados do database
@app.route("/reseta", methods=['POST'])
def resetar():
    database['ALUNO'] = []
    database["PROFESSOR"] = []
    return jsonify(database)

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug=True)