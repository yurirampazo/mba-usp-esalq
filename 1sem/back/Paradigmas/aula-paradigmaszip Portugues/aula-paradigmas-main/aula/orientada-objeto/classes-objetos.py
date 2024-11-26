class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo= modelo
        self.ano = ano


    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo} {self.ano}")
        self.emitir_som()

    def emitir_som(self):
        print("vrumm")


carro1 = Carro(marca='Toyota', 
               modelo='Corolla',
               ano= 2020)

carro2 = Carro(marca='Renault', 
               modelo='Duster',
               ano= 2023)

carro1.exibir_detalhes()
carro2.exibir_detalhes()