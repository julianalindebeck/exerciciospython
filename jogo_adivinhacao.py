import random 

print('Seja bem-vindo ao jogo de adivinhação numérica!')
numero_usuario = input('Digite o número inteiro teto para começar o jogo: ')

while numero_usuario.isdigit() == False:
    numero_usuario = input('\nValor inválido! Digite um número inteiro: ')

numero_usuario = int(numero_usuario)

numero_aleatorio = random.randint(0, numero_usuario)

while True:
    escolha_usuario = input('\nAdivinhe o número escolhido pelo computador: ')

    if escolha_usuario.isdigit():
        escolha_usuario = int(escolha_usuario)
    else:
        print('\nValor inválido! Você deve escolher um número inteiro.')
        continue

    if escolha_usuario == numero_aleatorio:
        print('\nParabéns! Você acertou o número.')
        break
    elif escolha_usuario > numero_aleatorio:
        usuario_rejogar = input('Você errou o número! Seu número é maior que o escolhido pelo computador.' \
                                '\n\nDeseja tentar novamente? (S/N) ')
    else:
        usuario_rejogar = input('Você errou o número! Seu número é menor que o escolhido pelo computador.' \
                                '\n\nDeseja tentar novamente? (S/N) ')

    if usuario_rejogar != 'S':
        break
    else:
        continue

print('\nObrigada por jogar!')
