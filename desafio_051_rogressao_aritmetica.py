'''Exercício Python 51:
    Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os
10 primeiros termos dessa progressão.'''

print(f'\033[1;32m='*30)
print(f'{"10 Termos de uma PA":^30}')
print(f'\033[1;32m=\033[m'*30)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))# de quanto vai pular
decimo_termo = primeiro_termo + (10 - 1) * razao #formula do enésimo termo

for c in range(primeiro_termo, decimo_termo + razao, razao):
    print('{}'.format(c), end='-> ')
print('ACABOU')
