casos = int(input())
for i in range(casos):
    numero = int(input())
    personas = list(map(int, input().split()))
    ordenada = sorted(personas)
    res = 0
    while numero > 3:
        op1 = ordenada[0] + (2 * ordenada[1]) + ordenada[numero - 1]
        op2 = (2 * ordenada[0]) + ordenada[numero - 1] + ordenada[numero - 2]
        res = res + min(op1, op2)
        numero = numero - 2

    if numero == 3:
        res = res + sum(ordenada[0:3])
    elif numero == 2:
        res = res + ordenada[1]
    else:
        res = res + ordenada[0]
    print(res)