'''Exercício Python 27:
 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente.'''

nome = str(input('Nome completo: ')).strip()
print(f'Prazer em te conhecer {nome}')
print(f'Seu primeiro nome é {nome.split()[0]}')
print(f'Seu ultimo nome é {nome.split()[-1]}')
