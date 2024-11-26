class ContaBancaria:

    def __init__(self, titular, saldo_inicial = 0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor de deposito deve ser positivo")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valorS

conta_a = ContaBancaria(titular="Maria", saldo_inicial=200)
conta_b = ContaBancaria(titular="ALexandre", saldo_inicial=40000)

# print(conta_a.__saldo_inicial)  #Não compila, atributo está encapsulado
print(conta_a.get_saldo())

conta_a.depositar(2000)
print(conta_a.get_saldo())