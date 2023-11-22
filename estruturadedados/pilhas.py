pilha = []
pilha.append(10)
pilha.append(20)
pilha.append(30)
print("Topo da pilha", pilha[-1])
elemento_removido = pilha.pop()
print("elemento removido:",elemento_removido)
print("Topo da pilha", pilha[-1])
if not pilha:
    print("a pilha está vazia")
else:
 print("ainda tem elementos")


