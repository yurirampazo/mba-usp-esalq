# Usando real como ref
taxa_euro = 0.16
taxa_iene = 26.79

# Inputs em python sempre são strings
valor_real = float(input('Digite o valor em Reais: '))
print(type(valor_real))
print(f'Euro {valor_real * taxa_euro:.2f}')
print(f'Iene {valor_real * taxa_iene:.2f}')