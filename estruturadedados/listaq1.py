nomes= ["Luan", "Gustavo", "Ester", "iago"]
for nome in nomes:
    print(nome) 
    #procurar um nome na lista
if "vinicius" in nomes: 
    print("aluno está presente")
else:
    print("Aluno faltou")

    #concatenar outra lista
    outros_nomes =  ["helder", "aduyar"]
    todos_alunos = nomes + outros_nomes 
    print(todos_alunos)
                    