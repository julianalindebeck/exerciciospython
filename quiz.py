print('Seja bem-vindo ao quiz sobre música!')
resposta_usuario = input('Gostaria de iniciar o quiz? (S/N) ')

if resposta_usuario != 'S':
    quit()

pontuacao = 0

print('\nPrimeira pergunta: qual cantora lançou a música "Diamonds"?' \
      '\n(a) Ariana Grande \n(b) Beyoncé \n(c) Rihanna \n(d) Britney Spears')
resposta_1 = input('Digite sua resposta: ')

if resposta_1 == 'c':
    print('\nResposta correta!')
    pontuacao += 1
else:
    print('\nResposta incorreta! A alternativa certa era a letra (c).')

print('\nSegunda pergunta: qual o nome da clássica música de Natal da cantora Mariah Carey?' \
      '\n(a) Merry Christmas \n(b) All I Want For Christmas Is You \n(c) True Love \n(d) Snowflakes')
resposta_2 = input('Digite sua resposta: ')

if resposta_2 == 'b':
    print('\nResposta correta!')
    pontuacao += 1
else:
    print('\nResposta incorreta! A alternativa certa era a letra (b).')

print('\nTerceita pergunta: qual a nacionalidade da cantora Shakira?' \
      '\n(a) Colombiana \n(b) Brasileira \n(c) Peruana \n(d) Espanhola')
resposta_3 = input('Digite sua resposta: ')

if resposta_3 == 'a':
    print('\nResposta correta!')
    pontuacao += 1
else:
    print('\nResposta incorreta! A alternativa certa era a letra (a).')

print(f'\nVocê terminou o quiz! Sua pontuação foi {pontuacao}/3. Obrigada por jogar!')
