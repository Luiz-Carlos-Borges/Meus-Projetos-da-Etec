import os
os.system ('cls')

print("Vamo Jokenpô 3 liguinha")
import random
itens = ["pedra", "papel", "tesoura"]
computador = random.choice (itens)
jogador = int(input("Escolha sua opção: [0] pedra, [1] papel, [2] tesoura"))
print("O computador escolheu", format(computador))