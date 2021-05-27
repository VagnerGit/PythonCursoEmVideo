'''Exercício Python 10: Crie um programa que leia quanto dinheiro uma
pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''

r = float(input('Quantos Reais quer converter em Dolar '))
#d = r*3.27
print('Com R${:.2f} Você compra ${:.2f}'.format(r, (r/3.27)))
