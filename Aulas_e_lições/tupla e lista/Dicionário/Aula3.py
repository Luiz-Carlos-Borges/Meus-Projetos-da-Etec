Brasil=[]
Estado={'UF':'Rio de Janeiro', 'Sigla':'RJ'}
Estado2={'UF':'São Paulo', 'Sigla':'SP'}

Brasil.append(Estado)#Adiciona a lista no dicionario
Brasil.append(Estado2)

print(Brasil)
print(Brasil[0])#mostra a priemira
print(Brasil[1])
print(Brasil[0]['UF'])
print(Brasil[1]['UF'])

materia=dict()
curso=list()
for c in range (0,3):
    materia['Sigla'] = str(input('Digite a Sigla  da Materia-->'))
    materia['nome'] = str(input('Digite o nome da Materia-->'))
    curso.append(materia.copy()) #vai fazer uma cópia do dicionário
    print(curso)

    for m in curso:
        for k, v, in m.items():
            print(f'o campo {k} tem o valor {v}')

            lista=[]
            dic=dict()

            nome=input('Digite-->')
            idade=input('Digite-->')

            lista.append(nome)
            lista.append(idade)

            dic={'nome':lista[0], 'idade':lista[1]} #adiciona uma lista dentro de um dicionário
            print(lista)
            print(dic['nome'])