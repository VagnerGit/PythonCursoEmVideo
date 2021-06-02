'''Exercício Python 29:
 Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km
acima do limite.'''

velocidade = float(input("\33[7:30m Infomer velocidade do veiculo?\33[m "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Velocidade {} {:.0f}km/h {} superior a 80km/h\n você foi {} multado em R${:.2f}{}'
          .format('\033[1:31m', velocidade, '\033[m', '\033[4:31m', multa, '\033[m'))
print('\033[:32:45m Dirija com responsabilidade\033[m')

