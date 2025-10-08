import os
os.system('cls')
'''

compras=['arroz','feijão','alho','ovo','leite','chocolate']
print(compras)

compras[3]='frango'

print('\n',compras)

compras[1]='feijoada'

print('\n',compras)

compras.append('café')# vai adicionar no final da lista

print('\n',compras)

compras.insert(0,'batata')# adiciona na pocição desejada

print('\n',compras)

del compras[3] # ou compras.pop(3) ou compras.remove('alho')

print('\n',compras)
'''
'----------------------------------------------------'
'''
if 'chocolate' in compras:

    compras.remove('chocolate') #caso tente remover um item que não existe ele dá erro (obviamente) OBS: não adeicionar duas vezes o mesmo comando, porque ele vai dar erro

    print('\n',compras)
'2'
valores=list(range(4,11))# ou valores=[4,5,6,7,8,9,10] cira uma lista

print('\n',valores)

numeros=list(range(0,11))

numeros.sort()#lista na ordem crescente

print('\n',numeros)

numeros.sort(reverse=True)#lista na ordem decrescente

print('\n',numeros)

val=[] #ou val=list() cia uma lista vazia

print('\n',val)

val.append(5)
val.append(9)
val.append(6)

print('\n',val)

for v in val: # vai fazer um colocação de numeros
    print(f'\n {v}...')
    print(f'\n {v}...', end='') #tira um e mostra o seguinte e após isso ele deleta o anterior

for c,v in enumerate(val):
    print(f'\n na pociçao {c+1} encontrei o valor {v}!')
    print('\n cheguei ao final da lista!')


lista_usu=list() # vai fazer um colocação de numeros a partir dos números que você digitou

for cont in range(0,5):
    lista_usu.append(int(input('\n Digite um valor aqui vilão-->')))

    for c,v in enumerate(lista_usu):
     print(f'na pociçao {c+1} encontrei o valor {v}!')
    print(' cheguei ao final da lista!')
'''
'----------------------------------------------------------'

a=[2,4,5]
b=a #cria duas listas iguais

print(f'lista A = {a}')
print(f'lista B = {b}')

b[2] = 8 # vai alterar o valor 2
print(f'lista A = {a}')
print(f'lista B = {b}')

a=[2,4,5]
b=a[:] #só vai alterar a lista 'b'

b[2] = 8
print(f'lista A = {a}')
print(f'lista B = {b}')






