#input
M=int(input())
m=input()
N=int(input())
n=input()
x=list(map(int,m.split()))
y=list(map(int,n.split()))
a=set(x)
b=set(y)
c=a-b
d=b-a
e=c|d
result=list(e)
result.sort()
for i in range(len(result)):
    print(result[i])