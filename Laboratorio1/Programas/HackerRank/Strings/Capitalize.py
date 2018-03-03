def capitalize(string):
    s = string.split(" ")
    lista = []
    for i in s:
        res = i.capitalize()
        lista.append(res)
    resp = " ".join(lista)
    return resp