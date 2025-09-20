import os
import time
os.system("cls")

print("Contagem regressiva para o ano novo!")
for c in range (10,0,-1):
    print(c)
    time.sleep(1) # espera 1 segundo antes de mostrar o próximo número
print("Feliz Ano Novo!")
