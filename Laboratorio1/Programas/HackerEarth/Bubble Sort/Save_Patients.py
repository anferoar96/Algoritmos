pac = int(input())
vacunas = list(map(int,input().split()))
pacientes = list(map(int,input().split()))
con = "Yes"
for i in range(pac):
    if vacunas[i] >= pacientes[i]:
        continue
    else:
        con = "No"
        break
print(con)