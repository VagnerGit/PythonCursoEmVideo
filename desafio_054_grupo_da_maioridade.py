'''Exercício Python 54:
    Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date

ano = date.today().year
cont = 0
contmenor = 0

for c in range(1, 8):
    nasc = int(input('Em que ano a \033[33m{}º\033[m pessoa nasceu: '.format(c)))
    idade = ano - nasc
    if idade >= 21:
        cont += 1
        print('A \033[32m{}ª\033[m pessoa é maior de idade com {}{}{}'.format(c, '\033[32m', idade, '\033[m'))
        print()
    else:
        contmenor += 1
        print('A \033[31m{}ª\033[m pessoa não é maior de idade com {}{}{}'.format(c, '\033[31m', idade, '\033[m'))
        print()

print('\033[32mVocê tem {} pessoas maior de idade\033[m'.format(cont))
print('\033[31mVocê tem {} pessoas menor de idade\033[m'.format(contmenor))
