def minion_game(string):
    cont = 0
    cont1 = 0
    for j in range(len(string)):
        if string[j] in "QWRTYPSDFGHJKLZXCVBNM":
            cont = cont + (len(string)-j)
        if string[j] in "AEIOU":
            cont1 = cont1 + (len(string)-j)
    if cont > cont1:
        print ("Stuart "+str(cont))
    elif cont < cont1:
        print ("Kevin "+str(cont1))
    else:
        print ("Draw")