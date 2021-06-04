'''Exercício Python 32:
Faça um programa que leia um ano qualquer e
 mostre se ele é bissexto.'''

from datetime import date
ano = int(input('\033[4:35m Digite um ano com 4 digitos para saber se é bissexto \033[m'))

if ano==0:
    ano = date.today().year #pega a data de hoje e usa só o ano

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:#formula do ano bissexto
    print('{} é um ano Bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))

