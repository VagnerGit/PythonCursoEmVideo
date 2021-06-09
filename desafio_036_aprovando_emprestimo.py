'''Exercício Python 36:
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''


print(f'\033[1;34m{"Minha casa analise de crétido":-^50}\033[m')
print(f'{"A prestação deve ser no maximo 30 % do salário":^50}')
print()
salario = casa = meses = 0

while True:#validando entrada
    valor_salario = str(input('Favor digite \033[34mseu salário\033[m sem os centavos: R$'))
    valor_da_casa = str(input('Favor digite \033[34mvalor da casa\033[m sem os centavos: R$'))
    quantidade_de_anos = str(input('Em \033[34mquantos anos\033[m de finaciamento: '))
    if valor_salario.isnumeric() and valor_da_casa.isnumeric() and quantidade_de_anos.isnumeric():
        salario = int(valor_salario)
        casa = int(valor_da_casa)
        meses = int(quantidade_de_anos) * 12
        break
    else:
        print('\033[31mDigite apenas número inteiros e sem centavos\033[m')

disponivel = salario * 0.30
parcelas = casa / meses
if parcelas <= disponivel:
    print()
    print(f'\033[4mBeleza pode comprar a casa em {meses} vezes de R${round(parcelas, 2)},00\033[m')
else:
    print()
    print(f'O valor da parcelas esta acima de 30% que é R$ {disponivel:.2f} aumente as parcelas')
