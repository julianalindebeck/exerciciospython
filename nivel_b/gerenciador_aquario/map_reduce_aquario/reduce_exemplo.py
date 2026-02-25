from functools import reduce

numeros = [1, 2, 3, 4, 5]

def soma(a, b):
    return a + b

print(reduce(soma, numeros))
# não é necessário converter para list pois o reduce já devolve um dado acessível
