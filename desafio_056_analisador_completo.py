"""
Exercício Python 56:
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm
menos de 20 anos.
"""
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulher_menos_de_20 = 0

print('')
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Olá qual é seu nome? ')).strip()
    idade = int(input('Sua idade: '))
    sexo = str(input('Qual seu sexo [M/F]? ')).strip()
    soma_idade = soma_idade + idade# somaidade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    elif sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    elif sexo in 'Ff' and idade < 20:
        total_mulher_menos_de_20 = total_mulher_menos_de_20 + 1 #totmulher20 += 1

media_idade = soma_idade / 4
print()
print('A média da idade é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_mais_velho))
print('E {} mulheres com menos de 20 anos'.format(total_mulher_menos_de_20))
