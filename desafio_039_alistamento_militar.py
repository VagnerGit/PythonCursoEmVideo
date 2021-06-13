'''Exercício Python 39:
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento.
    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

#minha solução
from datetime import date

sexo = int(input('''Qual seu sexo digite
        [1] para Masculino
        [2] para Feminino
         R: '''))
if sexo == 2:
    print('\033[35m}{\033[m'*18)
    print('\033[35mComo {} você não pode se alistar\033[m'.format('MULHER'))
    print('\033[7:35m}{\033[m' * 18)
else:
    ano = int(input('Em que ano você nasceu? '))
    idade = date.today().year - ano # variavel pega o ano atual e subtraia o ano digitado
    print('Sua idade é de {}{} anos{}'.format('\033[33:m', idade, '\033[m'))

    if idade == 18:
        print('\033[32mApresentece a junta miliar\033[m')
    elif idade < 18:
        print('\33[34mAinda falta {} anos para se apresentar em {}\033[m'
              .format(18-idade, (18-idade)+date.today().year))
    else:
        print('\033[7:31mJá deveria ter se apresentado a {} anos em {}!\033[m'
              .format(idade-18, (18-idade)+date.today().year))

