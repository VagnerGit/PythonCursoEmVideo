'''Exercício Python 34:
Escreva um programa que pergunte o salário de um
funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Qual é salario? R$'))

if salario > 1250:
    novo = salario * 1.10 #salário*10/100
else:
    novo = salario * 1.15 #salário*15/100

print('Seu salário de {}{:.2f}{} agora é {}R${:.2f}{}'.format('\033[33m', salario, '\033[m', '\033[34m', novo, '\033[m'))
