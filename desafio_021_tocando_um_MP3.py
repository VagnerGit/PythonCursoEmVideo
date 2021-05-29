'''Exercício Python 21:
Faça um programa em Python que abra e reproduza o áudio de
um arquivo MP3.'''

import pygame
pygame.init()
pygame.mixer.music.load('ex21.mp3')# arquivo mp3 salvo na pasta do programa
pygame.mixer.music.play()
pygame.event.wait()
