import os
os.system('cls' if os.name == 'nt' else 'clear')

ip=int(input("Digite um número--> "))
if ip%2==0: #se o resto da divisão por 2 for 0, é par
    print("O número é par")
else:
    print("O número é ímpar")
