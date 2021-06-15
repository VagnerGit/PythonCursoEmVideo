'''Exercício Python 42:
    Refaça o DESAFIO 35 dos triângulos,acrescentando o recurso de mostrar que tipo de triângulo
será formado:'''

r1 = float(input('\033[36mdigite comprimento da 1º reta '))
r2 = float(input('digite comprimento da 2º reta '))
r3 = float(input('digite comprimento da 3º reta\033[m '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if r1 == r2 == r3:
        print('\033[1:34m EQUILÁTERO! \033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1:34m ESCALENO! \033[m')
    else:
        print('\033[1:34m ISÓSCELES! \033[m')
else:
    print()
    print('\033[31m ñ é triangulo \033[m')
