import json
import os
from functools import reduce

def seleciona_tipo_animal(animal):
    return animal["tipo"], 1

def reducer(acc, val):
    if val[0] not in acc.keys():
        acc[val[0]] = 0 + val[1]
    else:
        acc[val[0]] = acc[val[0]] + val[1]
    return acc

base = os.path.dirname(__file__)
caminho = os.path.join(base, '../aquario.json')

with open(caminho, encoding = 'utf8') as arq:
    data_aquario = json.load(arq)

animais = data_aquario["data"]

tipo_animais = list(map(seleciona_tipo_animal, animais))

print(tipo_animais)
print(reduce(reducer, tipo_animais, {}))
