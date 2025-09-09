import os
os.system('cls' if os.name == 'nt' else 'clear')

salario = float(input("Digite o salário--> "))
if salario > 2000:
    aumento = str(input("Você quer mais 15% de bônus? "))
    if aumento.lower() == "sim":
        salario1 = salario * 1.15
        print("Seu novo salário é de R$", salario1)
else:
    filhos = str(input("Você tem filhos?--> "))
    if filhos.lower() == "sim":
        quantos = int(input("Quantos filhos você tem?--> "))
        salario2 = salario + (quantos * 300)
        print("Seu novo salário é de R$", salario2)