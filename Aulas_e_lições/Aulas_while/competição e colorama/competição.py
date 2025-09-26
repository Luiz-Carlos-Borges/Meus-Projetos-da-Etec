import os
import random
os.system('cls')

print('Processo seletivo para substituir a Thais Carla')
print('Thais atualmente pesa 148 Kg')

pesos = [random.randrange(60, 250) for _ in range(5)] # gera 5 pesos aleatórios entre 60 e 250
# pesos = [candidato1, candidato2, candidato3, candidato4, candidato5

for i, peso in enumerate(pesos, 1): #enumerate para ter o índice (i) e o peso
    print('O candidato', i, 'pesa', peso, 'Kg') # imprime o peso do candidato
    if peso > 148:
        print('O candidato', i, 'foi aprovado')
    else:
        print('O candidato', i, 'foi reprovado')

# Verifica quem ficou em primeiro lugar entre os aprovados
aprovados = [(i+1, peso) for i, peso in enumerate(pesos) if peso > 148] # lista de tuplas (candidato, peso) dos aprovados
if aprovados:
    vencedor = max(aprovados, key=lambda x: x[1]) # pega o candidato com o maior peso
    print('O candidato', vencedor[0], 'ficou em primeiro lugar com', vencedor[1] , 'Kg') # imprime o vencedor
else:
    print('Nenhum candidato foi aprovado')