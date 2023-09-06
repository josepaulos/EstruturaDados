#Criar o dicionario
dic = { 'a' : 1, 'b' : 2, 'c' : 3 }
print('Dicionario',dic)
dic2={'d':4}
print('Dicionario2',dic2)

#imprime a quantidade de elementos do dicionario
print('tamanho de dicionario:',len(dic),'elemento(s)')
#Verifica se a chave a está no dicionario
print('a'in dic)
#verifica se a chave e não está no dicionario
print('e' not in dic)
#Deleta o elemento do dicionario chave b 
del(dic['b'])
#Retorna a lista de chaves do dicionario dic 
print(dic.keys())
#Retorna a lista de valores do dicionario dic
print(dic.values())
#Retorna a lista de puplas (chave, valor) do dicionario dic
print(dic.items())
#Imprime o novo dicionario
print('Novo dicionário', dic)

#juntando dois dicionarios 
dic.update(dic2)
print('Junção dos dois dicionarios', dic)