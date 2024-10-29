print('tipo int ', 1, '=>', type(1))
print(int(50.33))

idade = '33'
print(type(idade))
print(type(int(idade)))

# print(idade + 2)  -> Error, can only concatenate str to idade
print(idade + str(2))

# tipo bool
print("Tipo bool ", True, False, "=>", type(True))
print('teste conversão de int para bool', type(bool(1)))

boole = 0
print('teste 2 ', bool(boole))
print('teste 3 ', bool(1))

# Tipo float
print('tipo float ', 23.45, '=>', type(23.45))

# Array ou lista
liste = [5, 2, 3]
print('tipo list ', liste , '=>', type(liste))
print('last item ', liste[-1])

# teste louco
print('nome' * 3)


# DICIONÁRIO
dicionario = {
    "id" : 1993,
    "nome": "Nome do dicionario"
}
print(dicionario)
print(dicionario['id'])
print(dicionario['nome'])

# Tupla
# listas imutaveis
tupla = (1,2,3,4)
print(tupla[2])
# print(tupla[5]) => IndexError: tuple index out of range
print(tupla[-1])

liste.remove(5)
print(liste)

for numero in liste :
    print('For each liste', numero + 1)
    
if 3 in liste:
    print('A lista contém o número 3')
else:
    print('A lista nao contém o valor 3')