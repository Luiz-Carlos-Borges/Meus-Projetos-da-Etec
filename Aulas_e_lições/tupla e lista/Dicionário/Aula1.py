import os
os.system ('cls')
#lista={'joão','pedro','luiz'} #isso é um Dicionário
#lista=dict() #Cria um dicionário vazio
lista={'nome':'Pedro','idade':25}
print(lista['nome'])
print(lista['idade'])
print(f'{lista['nome']}, sua idade é {lista['idade']} anos')

lista['sexo']='3 vezes ao dia' #vai adicionar mais um indice na lista
print(lista['sexo'])
del lista['idade']
print(lista)