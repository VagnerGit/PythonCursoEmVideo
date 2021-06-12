'''Exercício Python 038:
    Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais'''

numero1 = float(input('Digite 1º Nº: '))
numero2 = float(input('Digite 2º Nº: '))
if numero1 > numero2:
    print(f'\033[0;33mO primeiro 1º Nº [{numero1}] é maior que o 2º [{numero2}].\033[m')
elif numero2 > numero1:
    print(f'\033[0;33mO segundo 2º Nº [{numero2}] é maior que o 1º [{numero1}].\033[m')
else:
    print(f'\033[0;33mO 1º e o 2º Nº são iguais [{numero1}] = [{numero2}].\033[m')
