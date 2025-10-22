filmes={'Titulo':'Velocipastor',
        'Ano':'2017',
        'Diretor':'Brendan Steere'}

print(filmes.values()) #mostra só os valores da lista
print(filmes.keys()) #mostra só os as chaves da lista
print(filmes.items()) #mostra os valores e as chaves da lista, mas você pode usar só o nome da variavel
    
for k,v in filmes.items():
    print(f'o {k} é {v}') #mosta a lista completa mais o texto

    pessoas={'nome':'Asdrubal','idade':'19','sexo':'f'}
print(f'A {pessoas['nome']} tem {pessoas['idade']} anos')

for k,v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
for k,v in pessoas.items():
    print(f'{k} = {v}')

pessoas['nome']='Ronaldo'
for k,v in pessoas.items():
    print(f'{k} = {v}')

pessoas['peso']=95
for k,v in pessoas.items():
    print(f'{k} = {v}')