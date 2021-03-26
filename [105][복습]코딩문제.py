##정확한 순위
#내가쓴 코드
n,m=map(int,input().split())
a=[[0]*n for _ in range(n)]

for _ in range(m):
    z1,z2=map(int,input().split())
    a[z1-1][z2-1]=1

for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[j][i]!=0 and a[i][k]!=0:
                a[j][k]=1

for i,v in enumerate(a):
    for j,v2 in enumerate(v):
        if v2==1:
            a[j][i]=1

r=0
for i in a:
    if i.count(1)==n-1:
        r+=1
print(r)
