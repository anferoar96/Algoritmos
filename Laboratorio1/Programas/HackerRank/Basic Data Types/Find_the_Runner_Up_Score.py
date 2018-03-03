n = int(input())
arr = map(int, input().split())
lista = tuple(arr)
ma = -200
me = -200
for i in lista:
    if i > ma:
        me = ma
        ma = i
    elif i > me and i != ma:
        me = i

print(me)