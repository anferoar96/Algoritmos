def wrap(string, max_width):
    l = len(string)
    lista = []
    s = ""
    for i in string:
        if len(s) < max_width:
            s += i
        else:
            lista.append(s)
            s = i
    if len(s) != 0:
        lista.append(s)
    resultado = "\n".join(lista)
    return resultado