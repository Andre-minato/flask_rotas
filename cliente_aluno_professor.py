import requests


def entradaDados():
    nome = input("Digite o nome: ") 
    id_aluno = int(input("Digite o id: "))
    
    dados = {"nome": nome, "id": id_aluno}
    
    return dados


def testePost():
	dados = entradaDados()
	x = requests.post("http://localhost:5002/adicionando_alunos", json = dados)
	if x.status_code != 200:
		print(f"[{x.status_code}] {x.text}")
	else:
		print(x.text) 
	
def testePut():
	id_aluno = int(input('Digite o id do aluno que deseja alterar: '))
	dados = entradaDados()
	x = requests.put("http://localhost:5002/alunos/"+str(id_aluno), json = dados)
	if x.status_code != 200:
		print(f"[{x.status_code}] {x.text}")
	else:
		print(x.text) 

def testeGetId():
	id_aluno = int(input('Digite o id do aluno que deseja buscar: '))
	x = requests.get("http://localhost:5002/alunos/"+str(id_aluno))
	if x.status_code != 200:
		print(f"[{x.status_code}] {x.text}")
	else:
		print(x.json()) 	


def testeGetNome():
	nome = input('Digite o nome do aluno que deseja buscar: ')
	x = requests.get("http://localhost:5002/alunos/"+nome)
	if x.status_code != 200:
		print(f"[{x.status_code}] {x.text}")
	else:
		print(x.text) 	
        
def testeDelete():
	id_aluno = int(input('Digite o id do aluno que deseja excluir: '))
	x = requests.delete("http://localhost:5002/alunos/"+str(id_aluno))
	if x.status_code != 200:
		print(f"[{x.status_code}] {x.text}")
	else:
		print(x.text) 		

print('------------------------------------------\n')		
print('Testando a rota /alunos com POST\n')
testePost()

print('------------------------------------------\n')	
print('Testando a rota /alunos com POST novamente \n')	
testePost()

print('------------------------------------------\n')	
print('Testando a rota /alunos com PUT \n')	
testePut()	
	
print('------------------------------------------\n')	
print('Testando a rota /alunos com GET e id do aluno\n')	
testeGetId()

print('------------------------------------------\n')	
print('Testando a rota /alunos com GET e nome do aluno\n')	
testeGetNome()

print('------------------------------------------\n')	
print('Testando a rota /alunos com DELETE\n')	
testeDelete()

