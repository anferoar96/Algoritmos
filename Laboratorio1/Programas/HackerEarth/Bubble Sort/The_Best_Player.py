lista = list(map(int,input().split()))
fans = lista[0]
maximo = lista[1]
li = []
for i in range(fans):
    d = input().split()
    d[1] =  int(d[1])
    li.append(d)
sorteada = sorted(li,key=lambda x: (-x[1],x[0]))
for j in range(len(sorteada[:maximo])):
    print (sorteada[j][0])