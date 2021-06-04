'''Exercício Python 33:
Faça um programa que leia três números e mostre qual é o maior e
qual é o menor.'''

from time import sleep

n1 = int(input('\033[1:32mDigite 1º Nº inteiro\33[m '))
n2 = int(input('\033[1:34mDigite 2º Nº inteiro\33[m '))
n3 = int(input('\033[7:32mDigite 3º Nº inteiro\33[m '))

menor = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
sleep(1)
print('\033[7:37m-=-\033[m'*15)
print("O menor Nº entre {}{}{}, {}{}{} e {}{}{} é {}{}{}"
      .format('\033[30m', n1, '\033[m', '\033[32m', n2, '\033[m ', '\033[36m', n3,
              '\033[m', '\033[1:34:40m', menor, '\033[m'))

maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
sleep(1)
print('\033[7:37m-=-\033[m'*15)
print("O maior Nº entre {}{}{}, {}{}{} e {}{}{} é {}{}{}"
      .format('\033[30m', n1, '\033[m', '\033[32m', n2, '\033[m ', '\033[36m', n3,
              '\033[m', '\033[1:34:40m', maior, '\033[m'))

