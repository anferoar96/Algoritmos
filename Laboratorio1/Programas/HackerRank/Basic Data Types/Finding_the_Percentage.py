n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
li = student_marks[query_name]
a = len(li)
total = 0
for i in li:
    total += i
res = total/a
print("%.2f" % res)