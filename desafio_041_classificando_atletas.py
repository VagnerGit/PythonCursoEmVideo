'''Exercício Python 041:
    A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificaçõa: MIRIM')
elif idade <= 14:
    print('Classificaçõa: INFANTIL')
elif idade <= 19:
    print('Classificaçõa: JUNIOR')
elif idade <= 25:
    print('Classificaçõa: SÊNIO')
else:
    print('Classificaçõa: MASTER')
