class Despesa:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

despesasEster = []
totalGasto = 0

while True:
    nome_despesa = input("Digite o nome da despesa ou sair para encerrar: ")

    if nome_despesa.lower() == 'sair':
        break

    valor_despesa = float(input("Digite o valor de despesa: "))

    despesa = Despesa(nome_despesa, valor_despesa)
    despesasEster.append(despesa)
    #total_gasto = total_gasto + valor_despesa

    totalGasto += valor_despesa

    print("\nLista de despesas da Ester: ")
    for i in despesasEster:
        print(f"{i.nome}: R$ {i.valor: .2f}")

    print(f"\n Total gasto: R$ {totalGasto: .2f}")