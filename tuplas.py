#tupla de string
exemplo = ('a','b','c','d','e')
#retorna elementos do ídice 1 até o índice2
print(exemplo[1:3])
#retorna elementos do inicio até o índice2
print(exemplo[:3])
#retorna elementos do índice 3 ate o final
print(exemplo[3:])



#soma de Tuplas
exemplo2 = ('z','y')+('x',)
#imprime a tupla após a soma
print('imprime a tupla após a soma',exemplo2)
#soma tuplas
exemplo2 +=(3,)
#imprime a tupla após a nova soma
print('imprime a tupla após nova a soma',exemplo2)
#retorna multiplicação da tupla
print('retorna multiplicação da tupla',exemplo2*2)

#tipo a tupla
print(type(exemplo2))
print(type(exemplo))
