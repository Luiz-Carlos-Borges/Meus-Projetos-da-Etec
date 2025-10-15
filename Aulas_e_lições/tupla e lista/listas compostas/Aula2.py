import os
os.system('cls')

turma=[['Ana',15],['João',20],['Pedro',32],['Raul',44]]
print(turma)
print(turma[0])
print(turma[1][1])

for p in turma:
    print(p)#ordena um abaixo do outro

for p in turma:
    print(p[0])#mostra somente os itens da primeira posição

for p in turma:
    print(p[1])#mostra somente os itens da segunda posição

for p in turma: 
    print(p[0],'tem',p[1],'anos de idade')#acrescenta a lista o texto e organiza ela

for p in turma: 
    print(f'\n{p[0]},tem,{p[1]},anos de idade\n')