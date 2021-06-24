'''Exercício Python 48:
    Faça um programa que calcule a soma entre todos os números que são múltiplos de três e
que se encontram no intervalo de 1 até 500.'''

soma = 0
contador = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        contador += 1

print()
print('''A soma entre todos os números que são múltiplos de três e que
 se encontram no intervalo de 1 até 500''')
print(f'\033[4;36mSão {contador} e a soma é {soma:=^11}\033[m')
