import os
os.system('cls')

numeros = []
pares = []
impares = []

print('Seja Bem-vindo!')
print('\nVamos digitar seu cadastro')

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