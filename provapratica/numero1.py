#  Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
#Em seguida, calcule a média anual das temperatura e mostre a média calculada juntamente com todas as temp 
#acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).



meses = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro",]
temp= []

for i in range(12):
    temp.append(
        float(input(f"DIgite a temperatura de {meses[i]}"))
        )
print(meses)
print(temp)

#media
media =sum(temp)/12
print("a media da temperatura anual foi",media," em ºC")
#mostrar os meses e suas respectivas temperaturas
for i in range(12):
    print(f"Mes:{meses[i]} Temperatura{temp[i]}ºC")