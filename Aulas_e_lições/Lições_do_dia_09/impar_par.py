import os
import random
os.system ('cls')

print("Vamo impar ou par")
escolha = str(input("Escolha impar[i] ou par[p]"))
num = int(input("Digite um numero: "))
computador = random.randint(0,10)
total = num + computador
if total % 2 == 0:
    print(f"Você jogou {num} e o computador {computador}. {total}, deu par")
    if escolha == 'p':
        print("Voce ganhou")
    else:
        print("Voce perdeu")
else:
    print(f"Você jogou {num} e o computador {computador}. {total}, deu impar")
    if escolha == 'i':
        print("Voce ganhou")
    else:
        print("Voce perdeu")
