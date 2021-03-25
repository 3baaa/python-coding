##플로이드
#내가쓴 코드
#결과값이 나온다
n=int(input())
m=int(input())
a=[[int(1e9)]*n for _ in range(n)]

for _ in range(m):
    n1,n2,n3=list(map(int,input().split()))
    a[n1-1][n2-1]=min(a[n1-1][n2-1],n3)

for i in range(n):
    a[i][i]=0
    
for i in range(n):
    for j in range(n):
        for k in range(n):
            a[j][k]=min(a[j][k],a[j][i]+a[i][k])


for i in a:
    for j in i:
        if j==int(1e9):
            print(0,end=" ")
        else:
            print(j,end=" ")
    print()
