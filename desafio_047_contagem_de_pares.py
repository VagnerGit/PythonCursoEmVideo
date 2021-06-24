'''Exercício Python 47:
 Crie um programa que mostre na tela todos os
números pares que estão no intervalo entre 1 e 50.'''

print('\033[34m#Pares \033[m'*15)
print('Números pares que estão no intervalo entre 1 e 50.')
for c in range(0, 52, 2):
    print(c, end=' ')
print()
print()

print(f'\033[1;33m{"Agora digite um Número para ver os números pares que existem dentro dele":-^104}\033[m')
print('Contagem de pares')
numero = int(input('Digite um Nº inteiro para saber quantos pares existe dentro dele: '))
print()

if numero % 2 == 0:
    for c in range(0, numero + 1, 2):
        print(c, end=' ')
else:
    for c in range(0, numero, 2):
        print(c, end=' ')
