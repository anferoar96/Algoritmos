num = int(input())
numeros = list(map(int,input().split()))
par = []
impar = []
cont = cont1= 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        cont = cont + numeros[i]
        par.append(numeros[i])
    else:
        cont1 = cont1 +numeros[i]
        impar.append(numeros[i])
par.append(cont)
impar.append(cont1)
print (*(sorted(par)+sorted(impar)))