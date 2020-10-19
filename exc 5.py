'''
exc 5
Preencher uma lista com 3 nomes e mostrar quantas letras A e E tem nos 3 nomes.
'''
#Resolução do Exerc 5 por BOT-Samuel


lista10 = []
total = 0

for i in range(3):
    nomes = input("Digite um nome:")
    lista10.append(nomes)

for i in range(3):
    nome = lista10[i]
    for x in range(len(nome)):
        if (nome[x] == 'a' or nome[x] == 'A' or nome[x] == 'e' or nome[x] == 'E'):
            total = total + 1
print("="*30)

print ("Há {0} ocorrÊncias das letra E e A nos três nomes.".format(total))
