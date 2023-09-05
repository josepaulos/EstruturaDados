#listas de valores
notas =[0,10.0,7.0,7.0,8.0,8.0]
animais=['gato','tatu','rato','pato']
#insere o elemento da lista na posição
notas.insert(1,5.0)
print(notas)
notas.insert(2,6.0)
print(notas)
#remove os elementos
notas.remove(8.0)
print(notas)
notas.remove(7.0)
print(notas)

#metodo de soma 
print('A soma das notas:',sum(notas))
#metodo de maximo
print('A maior das notas:',max(notas))
#metodo de minino
print('A menor das notas:',min(notas))

#função append
notas.append(6.0)
#função extend
notas.extend(animais)



#notas.sort()


#print(sorted(notas)) 
print(notas)
