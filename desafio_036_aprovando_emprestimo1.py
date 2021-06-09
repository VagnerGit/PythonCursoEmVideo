'''Exercício Python 36:
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

salario = float(input('Qual o salário: R$'))
casa = float(input('Valor da casa: R$'))
parcela = int(input('Enquatos anos Você quer pagar: '))
vparcelas = casa / (parcela * 12)
saldo = salario*0.30
if vparcelas > saldo:
    print(f'Com salario de \033[4;33;40m{salario}\033[m não a margem para as parcelas de \033[1;31m{vparcelas:.2f}\033[m')
else:
    print(f'Parabens com salário de {salario} você pode fazer parcelas de {vparcelas:.2f}')
