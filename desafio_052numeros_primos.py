'''Exercício Python 52:
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

print(f'\033[1;33m>'*40)
print(f'{"Vamos ver se o número é primo":^40}')
print(f'\033[1;33m<\033[m'*40)

numero = str(input('Digite um número: ')).strip()
if numero.isalpha() or numero == '' or numero.count(' '):# validação da entrada
    print('digito invalido')

else:
    print(f'O número {numero} é divisivel pelos Nº \033[33mAMARELOS\033[m [', end=' ')
    contador = 0
    num = int(numero)
    for i in range(1, num+1):
        if num % i == 0:
            contador += 1
            print(f'\033[33m', end=' ')
        else:
            print(f'\033[31m', end=' ')
        print(f'{i}', end=' ')
    print(f'\033[m.]')
    if contador == 2:
        print(f'\033[33mO número {num} é primo\033[m')
    else:
        print(f'\033[31mO número {num} não é primo\033[m')
