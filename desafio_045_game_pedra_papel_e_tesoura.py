'''Exercício Python 45:
    Crie um programa que faça o computador jogar Jokenpô com você.'''

from emoji import emojize
from time import sleep
from random import randint
itens = ('\033[4;47mPedra\033[m', '\033[7;40mPapel\033[m', '\033[1;34;40mTesoura\033[m')
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

while True:# validando entrada do jogador

    jogador = str(input('Qual é a sua jogada? ')).strip()

    if jogador.isnumeric():
        jogador = int(jogador)
        if jogador in range(0, 3):
            break

    if jogador.isalnum() or jogador == '' or jogador.count(" "):
        print('Opção invalida')

print('\033[31mJO\033[m')
sleep(0.5)
print('\033[33m  QUEM\033[m')
sleep(0.5)
print('\033[32m      PÔ\033[m')
sleep(0.5)
print('-='*20)
print(f'O Computador jogou {itens[pc]}', end=' ')

if pc == 0: # escolha de EMOJI para PC
    print(emojize(":facepunch:", use_aliases=True))
elif pc == 1:
    print(emojize(":hand:", use_aliases=True))
else:
    print(emojize(":v:", use_aliases=True))
print(f'O Jogador    jogou {itens[jogador]}', end=' ')

if jogador == 0: # escolha de EMOJI para Jogador
    print(emojize(":punch:", use_aliases=True, variant="emoji_type"))
elif jogador == 1:
    print(emojize(":raised_hand:", use_aliases=True, variant="emoji_type"))
else:
    print(emojize(":v:", use_aliases=True, variant="emoji_type"))
print('-='*20)

if pc == 0: #jogou PEDRA
    if jogador == 0:
        print('\033[33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[36mJogador VENCEU!!!\033[m')
    elif jogador == 2:
        print('\033[33mComputador venceu\033[m')

if pc == 1:  # jogou PAPEL
    if jogador == 0:
        print('\033[33mComputador venceu\033[m')
    elif jogador == 1:
        print('\033[33mEMPATE\033[m')

if pc == 2:  # jogou TESOURA
    if jogador == 0:
        print('\033[36mJogador VENCEU!!!\033[m')
    elif jogador == 1:
        print('\033[33mComputador venceu\033[m')
    elif jogador == 2:
        print('\033[33mEMPATE\033[m')
