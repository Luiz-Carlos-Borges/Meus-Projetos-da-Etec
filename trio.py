import os
os.system('cls')

numeros = []
pares = []
impares = []

print('Seja Bem-vindo!')
print('\nVamos digitar seu cadastro')

while True:
    # Entrada dos números
    p = int(input('Digite o primeiro número do seu cadastro: '))
    s = int(input('Digite o segundo número do seu cadastro: '))
    t = int(input('Digite o terceiro número do seu cadastro: '))
    q = int(input('Digite o quarto número do seu cadastro: '))
    qi = int(input('Digite o quinto número do seu cadastro: '))
    sex = int(input('Digite o sexto número do seu cadastro: '))
    sete = int(input('Digite o sétimo número do seu cadastro: '))

    # Adiciona os números à lista principal
    numeros.extend([p, s, t, q, qi, sex, sete])

    # Classifica os números em pares e ímpares
    for n in [p, s, t, q, qi, sex, sete]:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    # Exibe os resultados
    print("\nMatrícula completa:", numeros)
    print("Números pares:", pares)
    print("Números ímpares:", impares)

    # Encerra o loop após o cadastro
    break