import os
os.system('cls' if os.name == 'nt' else 'clear')

ks=float(input("Qual o KM de saída do seu carro?"))
kc=float(input("Qual o KM de chegada?"))
hs=float(input("Quando você saiu?"))
hc=float(input("Quando você chegou?"))

media=ks-kc/hs-hc

if media<80:
print("multa de 5 reais para você amigo")

else:
print("continue na linha")