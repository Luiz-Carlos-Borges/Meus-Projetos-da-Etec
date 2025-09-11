import os
os.system ('cls')

print("Vamo impar ou par")
import random
itens = ["par", "impar"]
computador = random.choice (itens)
jogador = int(input("Escolha sua opção: [0] par, [1] impar: "))
print("O computador escolheu", format(computador))