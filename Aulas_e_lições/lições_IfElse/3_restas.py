import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Digite 3 retas e veremos se formam um triângulo")

reta1 = float(input("Reta 1--> "))
reta2 = float(input("Reta 2--> "))
reta3 = float(input("Reta 3--> "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2: #se cada reta for menor que a soma das outras duas
    print("As retas formam um triângulo")
else:
    print("As retas NÃO formam um triângulo")