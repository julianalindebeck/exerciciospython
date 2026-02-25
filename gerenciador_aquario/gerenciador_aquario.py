import json
import os

def nome_animal(animal):
    return animal["nome"]

def altera_tanque(animais, nomes_selecionados, novo_tanque):
    def muda_num_tanque(animal):
        if animal["nome"] in nomes_selecionados:
            animal["num_tanque"] = novo_tanque
        return animal
    return list(map(muda_num_tanque, animais))

base = os.path.dirname(__file__)
caminho = os.path.join(base, 'aquario.json')

with open(caminho, encoding = 'utf8') as arq:
    data_aquario = json.load(arq)

animais = data_aquario["data"]

animais_peixe = list(filter(lambda animal: (animal["tipo"] == 'peixe'), animais))
# filter "aplica" a função verifica_peixe para cada animal da lista

animais_peixe_nome = list(map(nome_animal, animais_peixe))
# map seleciona o nome dos animais que são peixes

novo_aquario = altera_tanque(animais, animais_peixe_nome, 42)

print(novo_aquario)