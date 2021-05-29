"""
Exercício Python 14:
    Escreva um programa que converta uma temperatura digitando em graus Celsius e
converta para graus Fahrenheit.
"""

print('\033[4:31mConversor Celsius e converta para graus Fahrenheit\033[m')
print()
t = float(input('Digite a temperatura em Cº: '))
f = 9*t / 5 + 32 #p/converte Cº p/ Fº
print('\033[33mCº=Fº\033[m  '*10)
print('{}{}Cº{} é igual {}{}Fº{}'.format('\033[36m', t, '\033[m', '\033[31m', f, '\033[m'))
