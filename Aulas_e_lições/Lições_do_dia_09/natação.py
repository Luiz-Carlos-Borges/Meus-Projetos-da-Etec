import os
os.system ("cls")

print("Bem-vindo à aula de natação!")
print("Vamos ver em qual categoria você se encaixa.")
idade = int(input("Por favor, insira sua idade-->"))
if idade <=9:
        print("Voc~e entra na categoria MIRIM")
elif idade <=14:
        print("Você se encaixa na categoria INFANTIL")
elif idade <=19:
        print("Você está na categoria JUNIOR")
elif idade <=25:
        print("Você se encaixa na categoria SÊNIOR")
else:
        print("Você se encaixa na categoria MASTER")