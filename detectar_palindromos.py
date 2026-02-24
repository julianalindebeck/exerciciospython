"""
def verifica_palindromo(palavra):
    j = len(palavra) - 1
    resultado = True

    for i in range(len(palavra)):
        if palavra[i] != palavra[j]:
            resultado = False
            break

        if i >= j:
            break

        j -= 1

        return resultado
"""
    
def verifica_palindromo_recursiva(palavra):
    if len(palavra) <= 1:
        return True
    else:
        return palavra[0] == palavra[-1] and verifica_palindromo_recursiva(palavra[1:-1])

palavra_usuario = input('Digite uma palavra: ')
palavra_formatada = palavra_usuario.lower()

eh_palindromo = verifica_palindromo_recursiva(palavra_formatada)

if eh_palindromo:
    print(f'\nA palavra "{palavra_usuario}" é um palíndromo.')
else:
    print(f'\nA palavra "{palavra_usuario}" não é um palíndromo.')
