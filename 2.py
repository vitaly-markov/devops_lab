n = int(input())
student_marks = {}
for num in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
for keys in student_marks:
    if keys==query_name:
     sum=0
     for i in range(len(student_marks[query_name])):
     sum = sum + float(student_marks[query_name][i])
x = float(sum/3)
print("%.2f"%x)
