import os
os.system('cls' if os.name == 'nt' else 'clear')

salario=float(input("Digite o salário--> "))
if salario>2000:
    aumento=str(input("você quer mais 15% de bônus?"))
    if aumento=="sim":
        salario1=salario*1.15
        print("Seu novo salário é de R$",salario1)
else:
    filhos=str(input("Você tem filhos?--> "))
    if filhos=="sim":
        salario2=salario-300  
        print("Seu novo salário é de R$",salario2)
    else:
        print("Seu salário permanece o mesmo.")
