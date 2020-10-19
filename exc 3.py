'''
exc 3
Preencher uma lista com números inteiros (8 unidades) solicitar um número do teclado. 
Pesquisar se esse número existe no vetor, usando o comando for. 
Se existir, imprimir em qual posição do vetor. Se não existir, imprimir MSG que não existe.
'''
#Resolução do Exerc 3 por BOT-Samuel

lista = []
ocorrencias = []
n = 0
for i in range(8):
    z = int(input("Digite um valor entre 0 e 10:"))
    if (z<0 or z>10):
        z = int(input("Digite novamente um valor SOMENTE entre 0 e 10:"))
    lista.append(z)

num = int(input("Qual nº entre 0 e 10 gostaria de verificar?"))

for i in range(8):
    if (lista[i] == num):
        ocorrencias.append(i)
        n = n + 1

if (n == 0):
    print("Não há ocorrências do número {0} na lista.".format(num))
else:
    print("Há {0} ocorrências do número {1} na lista, nas posições {2}.".format(n,num,ocorrencias[:]))
