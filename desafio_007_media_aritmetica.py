'''Exercício Python 7: Desenvolva um programa que leia as duas
notas de um aluno, calcule e mostre a sua média.'''

n1 = float(input('Digite nota AV: '))
n2 = float(input('Digite Nota AVS: '))
n3 = float(input('Digite nota VR: '))
#media = (n1+n2+n3)/3
print('A media do aluno é {:.1f}'.format((n1+n2+n3)/3))
