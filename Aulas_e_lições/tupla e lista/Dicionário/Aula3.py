Brasil=[]
Estado={'UF':'Rio de Janeiro', 'Sigla':'RJ'}
Estado2={'UF':'São Paulo', 'Sigla':'SP'}

Brasil.append(Estado)#Adiciona a lista no dicionario
Brasil.append(Estado2)

print(Brasil)
print(Brasil[0])
print(Brasil[1])
print(f'{Brasil[0]} {Brasil['UF']}')