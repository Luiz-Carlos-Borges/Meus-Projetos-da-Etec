import os
import random
os.system ('cls')

print("Vamo impar ou par")
escolha = str(input("Escolha impar[i] ou par[p]-->"))
num = int(input("Digite um numero-->"))
computador = random.randint(0,10)
total = num + computador 
if total % 2 == 0: 
    print("Você jogou", num, "e o computador", computador,".", total, "é par")
    if escolha == 'p' or 'par':
        print("Você ganhou")
    else:
        print("Você perdeu")
else:
    print("Você jogou", num, "e o computador", computador,".", total, "é impar")
    if escolha == 'i' or 'impar':
        print("Você ganhou")
    else:
        print("Você perdeu")
