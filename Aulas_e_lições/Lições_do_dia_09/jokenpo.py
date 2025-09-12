import os
os.system ('cls')

print("Vamo Jokenpô")
import random
itens = ["pedra", "papel", "tesoura"]
computador = random.choice (itens)
jogador = int(input("Escolha sua opção: [0] pedra, [1] papel, [2] tesoura: "))
print("O computador escolheu", format(computador))
if jogador == 0:
    if computador == "pedra":
        print("Empate")
    elif computador == "papel":
        print("Computador ganhou")
    elif computador == "tesoura":
        print("Jogador ganhou")
elif jogador == 1:
    if computador == "pedra":
        print("Jogador ganhou")
    elif computador == "papel":
        print("Empate")
    elif computador == "tesoura":
        print("Computador ganhou")
elif jogador == 2:
    if computador == "pedra":
        print("Computador ganhou")
    elif computador == "papel":
        print("Jogador ganhou")
    elif computador == "tesoura":
        print("Empate")