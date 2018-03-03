a = int(input())
for i in range(a):
    numeros = input().split()
    dif = int(numeros[0]) - int(numeros[1])
    num = list(map(int, input().split()))
    ordenada = sorted(num)
    minimo = sum(ordenada[:dif])
    maximo = sum(ordenada[-dif:])
    print(maximo - minimo)