import os
os.system('cls')

print('!separador de números inteiros!', end='')
print('\nOBS: não adicionar números negativos!\n')

numeros = [] # lista para armazenar todos os números
pares = [] # lista para armazenar os números pares
impares = [] # lista para armazenar os números ímpares

while True: # loop infinito, só para quando o usuário digitar -1
    n = int(input("Digite um número (ou -1 para parar)--> ")) # lê um número do usuário
    if n == -1: # se o número for -1, sai do loop
        break  
    numeros.append(n) # adiciona o número à lista completa
    if n % 2 == 0: # se o número for par
        pares.append(n) # adiciona à lista de pares
    else:   # se o número for ímpar
        impares.append(n) # adiciona à lista de ímpares

print("Lista completa:", numeros) # imprime a lista completa
print("Lista de pares:", pares) # imprime a lista de pares
print("Lista de ímpares:", impares) # imprime a lista de ímpares  12
