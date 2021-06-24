'''Exercício Python 49:
    Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando um laço for.'''

multiplicador = int(input('Digite um Nº ára ver a tabuada: '))
for n in range(0, 11):
    print(f'{multiplicador} x {n:2} = {multiplicador * n}')
