'''Exercício Python 040:
Crie um programa que leia duas notas de um aluno e calcule
sua média, mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''

n1 = float(input('Digite a 1ª de 0 a10 nota: '))
n2 = float(input('Digite a 2ª de 0 a10  nota: '))
n3 = float(input('Digite a 3ª de 0 a10  nota: '))
media = (n1+n2+n3)/3

if media <= 5.0:
    print('\033[31mSua media foi {:.1f} reprovado\033[m'. format(media))
elif 5.0 < media < 7:
    print('\033[33mSua media é {:.1f} você esta de recuperaçao\033[m'.format(media))
else:
    print('\033[36mSua media é {:.1f} PARABENS você passou\033[m'.format(media))
