'''Exercício Python 37:
    Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. '''


numero = int(input('Digite um Nº: '))
print('''Escolha uma das dases para conversão
[1]converter para BINÁRIO
[2]converter para OCTAL
[3]converter para HEXADECIMAL''')
escolha = int(input('Sua opção: '))

if escolha == 1:
    print(f'{numero} convertido para BINÁRIO é igaul a {bin(numero)[2:]}')
elif escolha == 2:
    print(f'{numero} convertido para OCTAL é {oct(numero)[2:]}')
elif escolha == 3:
    print(f'{numero} convertido para HEXADECIMAL é {hex(numero)[2:]}')
else:
    print('Escolha um Nº valido')
