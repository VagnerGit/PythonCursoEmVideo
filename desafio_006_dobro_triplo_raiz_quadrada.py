'''Exercício Python 006: Crie um algoritmo que leia um número e mostre o
seu dobro, triplo e raiz quadrada.'''
n = float(input("Digite um "))
#print(n*2,n*3,n**2)
do = n*2
tri = n*3
#raiz = n**2
raiz = n**(1/2)
soma = n+n
sub = n-n
div = n/2
divinteira = n//2
rest = n % 2
print('O dobro de {} é {};\no triplo é {};\na raiz quadrada é {};\na soma é {};\n'
      'a subtração é {};\na metade é {};\na metade inteira é {};\ne o reato da '
      'divisão é {}!' .format(n, do, tri, raiz, soma, sub, div, divinteira, rest))
