'''Exercício Python 50:
    Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

contador = 0
soma = 0
for i in range(1, 7):
    numeros = int(input(f'Digite o {i}º número: '))
    if numeros % 2 == 0:
        soma += numeros
        contador += 1
print(f'foi digitado(s) {contador} números pares e a soma entre eles foi {soma}')
