class estudante:
    def __init__(self,nome,idade,curso):
     self.nome = nome
     self.idade = idade
     self.curso = curso

#Criando uma instância de estudante

aluno1 = estudante("Jacó",98,"Moda")

print(aluno1.nome)
print(aluno1.idade)
print(aluno1.curso)

class contato:
    def __init__(self,nome,telefone,email):
     self.nome = nome
     self.telefone = telefone
     self.email = email

contato1 = contato("Jacó","04240028922","a.a@gmail.com")

print(contato1.nome)
print(contato1.telefone)
print(contato1.email)