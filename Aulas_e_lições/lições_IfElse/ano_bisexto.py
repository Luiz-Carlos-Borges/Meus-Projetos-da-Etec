import os
os.system('cls' if os.name == 'nt' else 'clear')

ano=int(input("Digite um ano-->"))
if (ano%4==0 and ano%100!=0) or (ano%400==0): #se o ano for divisível por 4 e não for divisível por 100, ou se for divisível por 400
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")