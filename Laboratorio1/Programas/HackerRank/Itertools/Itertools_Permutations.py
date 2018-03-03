from itertools import permutations
a = input().split()
for i in list(permutations(sorted(a[0]),int(a[1]))):
    print (*i,sep="")