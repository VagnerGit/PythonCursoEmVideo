'''Exercício Python 25:
 Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

nome = str(input('Nome completo vamos ver de tem Silva: ')).strip().lower()
#print(f'Seu nome tem Silva? {"silva" in nome}')
if 'silva' in nome:
    print('Parabens seu nome tem Silva.')
else:
    print('Infelismente seu nome não tem Silva.')

