import os
os.system("cls")

print("Vamos consultar a tabuada?")
num=int(input("Insira o valor desejado-->"))
for c in range(1,11):
    print(num, "x", c, "=", num*c)
