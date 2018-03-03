num = int(input())
lista = []
for i in range(num):
    word = input()
    lista.append([i + 1, word])

cont = 0
lis = []

for j in reversed(range(len(lista))):
    var = len(lista) - j - 1
    cont = 0
    for k in reversed(range(len(lista) - var)):
        if k > 0:
            if lista[k - 1][1] < lista[j][1]:
                cont += 1
    lis.append(cont)

for m in reversed(lis):
    print(m)