N = int(input())
lista = []
for i in range(N):
    str = input()
    s = str.split(" ")
    if s[0] == "append":
        lista.append(int(s[1]))
    elif s[0] == "remove":
        lista.remove(int(s[1]))
    elif s[0] == "sort":
        lista.sort()
    elif s[0] == "reverse":
        lista.reverse()
    elif s[0] == "pop":
        lista.pop()
    elif s[0] == "print":
        print (lista)
    else:
        lista.insert(int(s[1]),int(s[2]))