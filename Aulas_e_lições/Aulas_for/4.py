import os
os.system("cls")

i=int(input("Digite o inicio-->"))
f=int(input("Digite o fim-->"))
p=int(input("Digite o passo-->"))

for c in range (i,f+1,p): #faz com que ele conte a partir do número que você digitou e o "passo" faz com que ele pule conforme o número digitado (Exemlplo: 2,4,6,8,10)
    print(c)