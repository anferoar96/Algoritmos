casos = int(input())
for i in range(casos):
    tam = list(map(int,input().split()))
    lista1 = list(map(int,input().split()))
    lista2 = list(map(int,input().split()))
    cont = 0
    for j in range(tam[1]):
        if cont<tam[0]:
            if lista2[j]>lista1[cont]:
                print(lista2[j],end=" ")
            else:
                while lista2[j] < lista1[cont]:
                        print(lista1[cont],end=" ")
                        cont += 1
                        if cont==tam[0]:
                             break
                print(lista2[j],end=" ")
        else:
            print(lista2[j],end=" ")

    while(cont<tam[0]):
        print(lista1[cont],end=" ")
        cont +=1
    print()