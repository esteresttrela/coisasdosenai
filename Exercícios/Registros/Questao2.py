class Carro:
    def __init__(self, marca, modelo, anoFab):
     self.marca = marca
     self.modelo = modelo
     self.anoFab = anoFab

carro1 = Carro("fiat","gol","2000")
carro2 = Carro("gol","gol","2002")
carro3 = Carro("VW","go","2018")

carros = [carro1, carro2, carro3]

for cont in carros:
    print("Marca:", cont.marca)
    print("Modelo:", cont.modelo)
    print("Ano:", cont.anoFab)
    print()
