'''Exercício Python 26:
 Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a
letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a
última vez.'''

frase = str(input('Digite uma frase: ')).strip().lower()
print(f'Existem {frase.count("a")} letras [A].')
print(f'A 1º letra [A] aparece na posição {frase.find("a")+ 1}')
print(f'A ultima letra [A] aparece na posição {frase.rfind("a")+ 1}')

