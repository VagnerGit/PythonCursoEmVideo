"""
Exercício Python 15:
    Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

km = float(input("quantos Km foram roda dos? Km "))
dias = int(input('Quantos dias usou o carro? '))
pago = (dias*60)+(km*0.15)
print("{} dias, {}km, valor R${:.2f}".format(dias, km, pago))
