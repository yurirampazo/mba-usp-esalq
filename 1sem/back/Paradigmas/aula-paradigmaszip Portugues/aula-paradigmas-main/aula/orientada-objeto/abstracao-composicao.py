from abc import ABC, abstractmethod


class FormaGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        raise NotImplementedError("ESTE METODO DEVE SER IMPLEMENTADO")
    
class Circulo(FormaGeometrica):

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2

circulo = Circulo(raio=10)
area = circulo.calcular_area()
print(area)