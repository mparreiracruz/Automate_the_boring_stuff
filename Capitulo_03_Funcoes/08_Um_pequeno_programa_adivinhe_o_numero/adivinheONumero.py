#Este é um jogo de adivinhar o número.
import random

numeroSecreto = random.randint(1, 20)
print('Estou pensando em um número entre 1 e 20.')

#Peça ao jogador que adivinhe 6 vezes.
for adivinhacoes in range(1, 7):
    print('Faça uma adivinhação.')
    adivinhar = int(input())
    
    if adivinhar < numeroSecreto:
        print('Seu número é muito baixo.')
    elif adivinhar > numeroSecreto:
        print('Seu número é muito alto.')
    else:
        break #essa condição corresponde ao palpite correto!

if adivinhar == numeroSecreto:
    print('Muito bem! Você adivinhou meu número em ' + str(adivinhacoes) + ' adivinhações')
else:
    print('Não, o número que eu pensei era '+ str(numeroSecreto))
    