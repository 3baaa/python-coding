##플로이드##
'''
#내가쓴 코드#
#(결과값이 나온다)#
INF=int(1e9)
n=int(input())
m=int(input())

array=[ [INF]*(n+1) for _ in range(n+1) ]

for _ in range(m):
    a,b,c=map(int,input().split())
    if c<array[a][b]:
        array[a][b]=c

for i in range(1,n+1):
    array[i][i]=0
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            array[i][j]=min(array[i][j],array[i][k]+array[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        print(array[i][j],end=" ")
    print()

##정확한 순위##
#내가쓴 코드#
#(결과값이 나온다)#
INF=int(1e9)
n,m=map(int,input().split())

array=[[INF]*(n+1) for _ in range(n+1)]
c=[0]*(n+1)
t=[]
for _ in range(m):
    a,b=map(int,input().split())
    array[a][b]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            array[i][j]=min(array[i][j],array[i][k]+array[k][j])

result=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if array[i][j]==INF:
            if array[j][i]!=INF:
                c[i]+=1
        else:
            c[i]+=1
    if c[i]==5:
        result+=1

print(result)
'''
