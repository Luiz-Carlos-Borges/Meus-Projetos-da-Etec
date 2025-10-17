import os
os.system('cls')

numeros = []
pares = []
impares = []

print('Seja Bem-vindo!')
print('\nVamos digitar seu cadastro')

while len(numeros) < 7:  # O loop continuará enquanto houver menos de 7 números cadastrados
    try:
        n = int(input("Digite cada número do seu cadastro --> "))
        numeros.append(n)
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro.")

print("Cadastro completo!")
print("Lista completa:", numeros)
print("Lista de pares:", pares)
print("Lista de ímpares:", impares)