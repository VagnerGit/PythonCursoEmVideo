'''Exercício Python 31:
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
 e R$0,45 parta viagens mais longas.'''

v = float(input("\033[1:34m Sua viajem é de quantos quilometros?\033[m "))

if v <= 200:
    preço = v * 0.50
else:
    preço = v * 0.45

print("O volor da passagem é {:.2f}".format(preço))

