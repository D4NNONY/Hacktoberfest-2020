'''
exc 4
Preencher uma lista de 8 elementos inteiros. Mostrar o vetor na horizontal. Calcular a média do vetor. 
Mostrar quantos números são múltiplos de 5. Quantos números são maiores que 10 e menores que 30. Qual o maior número da lista?
'''
#Resolução do Exerc 3 por BOT-Samuel

lista = []
total = 0
media = 0
m5 = 0
ma10 = 0
me30 = 0
maior = 0
for i in range(8):
    w = int(input("Digite um valor entre 0 e 100:"))
    if (w<0 or w>100):
        w = int(input("Digite novamente um valor SOMENTE entre 0 e 100:"))
    lista.append(w)

print("="*30)

lista.sort()
print(lista[:])

for i in range(8):
    total = total + lista[i]
    media = total/8
    
for i in range(8):
    if (lista[i]%5 == 0):
        m5 = m5 + 1

for i in range(8):
    if  (lista[i]>10):
        ma10 = ma10 + 1

for i in range(8):
    if (lista[i]<30):
        me30 = me30 + 1

for i in range(8):
    if (lista8[i]>maior):
        maior = lista8[i]
print("="*30)

print ('''Na lista há {0} nºs múltiplos de 5, {1} nºs maiores que 10, {2} nºs menores que 30,
          o maior nº da lista é {3} e a média dos nºs da lista é {4}.'''.format(m5,ma10,me30,maior,media))


