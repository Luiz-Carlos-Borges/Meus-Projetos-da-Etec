import os
import random
os.system ('cls')

print("Vamo impar ou par")
escolha = str(input("Escolha impar[i] ou par[p]-->"))
num = int(input("Digite um numero-->"))
computador = random.randint(0,10) #gera um numero aleatorio entre 0 e 10
total = num + computador 
if total % 2 == 0: #verifica se o numero é par
    print("Você jogou", num, "e o computador", computador,".", total, "deu par")
    if escolha == 'p': #verifica se o usuario escolheu par
        print("Você ganhou")
    else:
        print("Você perdeu")
else:
    print("Você jogou", num, "e o computador", computador,".", total, "deu impar")
    if escolha == 'i': #verifica se o usuario escolheu impar 
        print("Você ganhou")
    else:
        print("Você perdeu")
