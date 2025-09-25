import os
import time

os.system('cls')

while True:
    pin = int(input("Digite o PIN-->"))
    if pin == 1234:
        for c in range(0, 100,5):
            time.sleep(0.2)
            print(c, 'verificando a senha', end='\r', flush=True)
        print('bem-vindo ao site para mães solteiras a 1km de distancia da sua casa')
        break
    else:
        for c in range(0, 100, 5):
            time.sleep(0.2)
            print(c, 'verificando a senha', end='\r', flush=True)
        print('senha incorreta, tente novamente')