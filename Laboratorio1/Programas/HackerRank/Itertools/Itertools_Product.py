from itertools import product
s = input().split()
m = input().split()
a = list(map(int, s))
b = list(map(int, m))


print(*product(a, b))