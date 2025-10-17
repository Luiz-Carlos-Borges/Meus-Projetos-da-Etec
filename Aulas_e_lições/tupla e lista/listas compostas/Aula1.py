#lista composta
import os
os.system('cls')

pessoas=[["joão",10],["Pedro",15],["josé",15]]
print(pessoas)
print(pessoas[0][0])#mostra o primeiro item da primeira posição
print(pessoas[1][1])#mostra o segundo item da segunda posição
print(pessoas[2])#mostra o segundo item


teste=list()
teste.append('lindolfo')
print(teste)
teste.append(43)
print(teste)

galera=list()
galera.append(teste[:])#adiciona a lista teste na lista galera, faz uma lista composta.
teste[0]='maria'#vai colocar por cima do resultado anterior
teste[1]=22#vai colocar por cima do resultado anterior
galera.append(teste[:])# O [:] torna uma lista idependente ou seja não importa a alteração ela não vai mudar
print(galera)
