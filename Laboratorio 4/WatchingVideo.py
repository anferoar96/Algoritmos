n, d = map(int, input().split())
datos = map(int, input().split())

tiempo = 0
maxtiempo = 0
cache = 0

for i in datos:
    tiempo += 1
    cache += i
    if cache >= d:
        if tiempo > maxtiempo:
            maxtiempo = tiempo
        tiempo = tiempo - 1
        cache = cache - d

print(maxtiempo)