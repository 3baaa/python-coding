##금광##
#내가쓴 코드#
#결과값이 나온다

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    t=list(map(int,input().split()))
    a=[[0]*m for _ in range(n)]
    dx=[1,0,-1]
    r=[0]*n
    k=0
    for i in range(n):
        r[i]=t[k]
        for j in range(m):
            a[i][j]=t[k]
            k+=1
    for i in range(n):
        x,y=i,0
        tx,ty=i,0
        for _ in range(1,m):
            b=[]
            z=0
            for k in range(3):
                nx=x+dx[k]
                ny=y+1
                if 0<=nx<n and z<a[nx][ny]:
                    z=a[nx][ny]
                    tx,ty=nx,ny;
            r[i]+=z
            x,y=tx,ny
    print(max(r))
