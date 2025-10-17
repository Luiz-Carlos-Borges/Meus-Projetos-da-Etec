import os
os.system('cls')

numeros=[]
pares=[]
impares=[]


print('seja Bem vindo!')
print('\nVamos digitar seu cadastro')

while True:









    e = (input("Digite seu cadastro--> "))
    if len(e) == 7:
        print("Bem-vindo")
    elif len(e) < 7:
        print("Entrada inválida:", e)
    else:
        print('Entrada inválida')






















        if e==e:
            numeros.append(e)
        if e % 2 == 0:
            pares.append(e)
        else: 
            impares.append(e)

        print("matrícula completa:", numeros)
        print("Números pares:", pares)
        print("Números ímpares:", impares) 