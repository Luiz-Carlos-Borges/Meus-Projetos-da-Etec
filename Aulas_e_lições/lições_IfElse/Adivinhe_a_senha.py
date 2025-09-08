import os
os.system('cls' if os.name == 'nt' else 'clear') #limpa o terminal #no Windows usa 'cls', no Linux/Mac usa 'clear'

pin=int(input("Digite o PIN-->"))
if pin==1234:
    print("Bem vindo ao sistema")
else:
    print("Vaza daqui zé ruela")