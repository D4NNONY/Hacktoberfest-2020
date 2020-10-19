'''
exc 2
Preencher uma lista de 8 elementos inteiros. 
Mostrar o vetor e informar quantos números são maiores que 30.
Somar todos os números.
'''
#Resolução do exerc 2 por BOT-Samuel

lista2 = []
t = 0
n = 0
for i in range(8):
    y = int(input("Digite um valor inteiro:"))
    lista2.append(y)

lista2.sort()
print(lista2[:])

for c in range(8):
    if (lista2[c]>30):
        n = n + 1
    t = t + lista2[c]
print ("Há {0} números maiores que 30 e a soma total dos nºs é {1}.".format(n,t))
