'''Exercício Python 44:
    Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''

print(f'{"LOJAS GUANABARA":=^40}')
preço = float(input('Preço das compras: R$'))
print('''FORMA DE PAGAMENTO
[1] à vista dinheiro/cheque;
[2] à vista cartão;
[3] 2x no cartão;
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preço - (preço * 10 / 100)
elif opcao == 2:
    total = preço - (preço * 0.05)
elif opcao == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opcao == 4:
    total = preço * 1.20
    total_de_parcelas = int(input('Quantas parcelas? '))
    parcelas = total / total_de_parcelas
    print(f'Sua compra será parcelada em {total_de_parcelas} de R${parcelas:.2f} com juros')
else:
    total = preço
    print('Opção inválida')
print(f'Sua compra de R${preço} vai custar R${total}')
