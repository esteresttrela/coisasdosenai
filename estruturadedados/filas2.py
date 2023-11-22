import queue 
#criar fila vazia
fila = queue.Queue()
fila.put("A")
fila.put("B")
fila.put("C")
#tamanho
tamanho = fila.qsize()
print("tamanho da fila:", tamanho)

#remover
item = fila.get()
print("item removido",item)
#será que removeu?
tamanho = fila.qsize()
print("tamanho da fila:", tamanho)
#verificar se a fila esta vazia
vazia = fila.empty()
print("a fila está vazia?", vazia)
