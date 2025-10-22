lista=[]
dic=dict()

nome=input('Digite-->')
idade=input('Digite-->')

lista.append(nome)
lista.append(idade)

dic={'nome':lista[0], 'idade':lista[1]} #adiciona uma lista dentro de um dicionário
print(lista)
print(dic['nome'])

dados={
    'crossfox': {'km': 3500, 'ano': 2005},
    'DS5': {'km': 17000, 'ano' : 2015},
    'fusca': {'km': 1300000, 'ano' : 1979},
    'Jetta': {'km': 56000, 'ano' : 2011},
    'Passat': {'km': 62000, 'ano' : 1999},  
}
for item in dados.items():
    print(item)
    for item in dados.items():
        print(item[1]['ano'])