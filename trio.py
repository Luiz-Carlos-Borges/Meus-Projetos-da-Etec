import os
os.system('cls')

numeros = []
pares = []
impares = []

print('Seja Bem-vindo!')
print('\nVamos digitar seu cadastro')

while True:
 
    p = int(input('Digite o primeiro número do seu cadastro: '))
    s = int(input('Digite o segundo número do seu cadastro: '))
    t = int(input('Digite o terceiro número do seu cadastro: '))
    q = int(input('Digite o quarto número do seu cadastro: '))
    qi = int(input('Digite o quinto número do seu cadastro: '))
    sex = int(input('Digite o sexto número do seu cadastro: '))
    sete = int(input('Digite o sétimo número do seu cadastro: '))

  
    numeros.extend([p, s, t, q, qi, sex, sete]) #extend adiciona vários elementos de uma vez enquanto o append acrescenta um elemento por vez

  
    for n in [p, s, t, q, qi, sex, sete]:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    print("\nMatrícula completa:", numeros)
    print("Números pares:", pares)
    print("Números ímpares:", impares)

    break