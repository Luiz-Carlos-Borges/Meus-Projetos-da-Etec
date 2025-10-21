import os
import time
os.system('cls')

user = 'professor'
senha = "1234"
contador = "s"  
print("=" * 100)
print("Boas-vindas à tela de login!")
print("=" * 100)

while contador == "s":
    user_novo = input("Qual seu usuário?: ")
    senha_novo = input("Qual a sua senha?: ")

    if user_novo == user and senha_novo == senha:

        for c in range(0,100, 5):
            time.sleep(0.5)
            print('Carregando o sistema...',c,'%', end='\r', flush=True)
    print('bem vindo ao sistema!')
    break  
else:
        print("=" * 100)
        print("Usuário ou senha incorretos.")
        print("=" * 100)
        contador = input("\nTentar novamente? (s/n): (nota: Digitar algo além de 's' acarretará no fim do programa.): ").lower()
        print("Obrigado por usar nosso programa.")
        print("=" * 100)
        print("Trabalho feito por:\n \nGustavo: encerramento \nVinicius: login \nLuiz: código\n")
        print("=" * 100)

      

numeros = []
pares = []
impares = []

print('=' * 100)
print('Seja Bem-vindo!')
print('\nVamos digitar seu cadastro')
print('=' * 100)

for i in range(1, 8): 
    n = int(input(f'Digite o {i}º número do seu cadastro: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\nMatrícula completa:", sorted(numeros))
print("Números pares:", sorted(pares))
print("Números ímpares:", sorted(impares))