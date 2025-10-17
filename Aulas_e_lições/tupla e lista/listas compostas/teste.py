import os
os.system('cls')

turma2=list()
dados=list()
totalmaior=totalmenor=0

for c in range(0,6):
    dados.append(str(input('Nome-->'.upper().strip())))
dados.append(str(input('Idade-->'.strip())))
turma2.append(dados[:])
dados.clear()
print(turma2)

while True:
    for p in turma2:
        if p[1] >=18:
            print(f'{p[0]} é maior de idade, ele tem {p[1]} anos de idade')
        totalmaior +=1
    else:
        print(f'{p[0]} é menor de idade, ele tem {p[1]} anos de idade')
        totalmenor +=1

        print(f'Temos {totalmaior} maiores de idade e {totalmenor} menores de idade')