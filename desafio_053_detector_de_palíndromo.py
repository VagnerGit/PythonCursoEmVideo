'''Exercício Python 53:
    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA.'''

#palindromos = ''
frase = str(input('Digite uma frase: ')).replace(" ", "").upper()
palindromos = frase[::-1]
# for i in reversed(frase):
#     palindromos += i
if frase == palindromos:
    print(f'''A frase \033[4;34m{frase}\033[m lida de trás para frente é igual a
     \033[4;36m{palindromos}\033[m por isso é um palíndromos''')
else:
    print(f'''A frase \033[4;34m{frase}\033[m lida de trás para frente é igual a
     \033[4;31m{palindromos}\033[m por isso \033[1;31mnão\033[m é um palíndromos''')
