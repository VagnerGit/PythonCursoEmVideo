'''Exercício Python 24:
 Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome
“SANTO”.'''

cid = str(input('Em que cidade você nasceu: ')).strip()
print(cid[:6].upper() == 'SANTOS')

'''
nome = str(input('Nome de Cidade: ')).lower().strip().split()
if nome[0] == 'santos':
    print(f'A cidade {nome} começa com {nome[0]}')
else:
    print(f'A cidade {nome} não começa com Santos.')
'''