numeros = int(input())
entrada = list(map(int, input().split()))
ordenados = sorted(entrada)
cont = 1
res = 0
for i in range(len(ordenados)):
    if i < (len(ordenados) - 1):
        if ordenados[i] == ordenados[i + 1]:
            cont += 1
        else:
            re = (cont * (cont - 1)) / 2
            res = res + re
            cont = 1

print(int(res))