"""Exercício Python 13:
 Faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário, com 15% de aumento.
"""

s = float(input("Quanto é o salário que vai receber 15% de aumento R$"))
a = round(s*1.15)#round arredonda
print('O novo salário é R$', a)
