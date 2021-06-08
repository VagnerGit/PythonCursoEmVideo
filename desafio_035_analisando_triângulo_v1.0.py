'''Exercício Python 35:
Desenvolva um programa que leia o comprimento de três retas e diga ao
usuário se elas podem ou não formar um triângulo.'''

a = float(input('\033[36mdigite comprimento da 1º reta '))
b = float(input('digite comprimento da 2º reta '))
c = float(input('digite comprimento da 3º reta\033[m '))

if a < b + c and b < a + c and c < a + b:
    print()
    print('\033[1:34m TRIANGULO \033[m')
else:
    print()
    print('\033[31m ñ é triangulo \033[m')
