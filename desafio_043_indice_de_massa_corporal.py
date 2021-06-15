'''Exercício Python 43:
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida '''

peso = float(input('Qual é seu peso: '))
altura = float(input('Qual é sua altura: '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}.')
if imc < 18.5:
    print('\033[31mVocê está ABAIXO DO PESO normal\033[m')
elif 18.5 <= imc < 25:
    print('\033[7;44mVocê está na faixa DO PESO normal\033[m')
elif 25 <= imc < 30:
    print('\033[4;33mVocê está com SOBREPESO\033[m')
elif 30 <= imc < 40:
    print('\033[1;31mVocê está em OBESIDADE, atenção!\033[m')
else:
    print('\033[7;37;41mVocê está em OBESIDADE MÓRBIDA, cuidado\033[m')
