##아기상어
#내가쓴 코드
#결과값이 나온다

from collections import deque

def check():
    t=[]
    for i in range(n):
        for j in range(n):
            if a[i][j]!=0 and shark_b>a[i][j]:
                x=shark_l[0]
                y=shark_l[1]
                b=abs(i-x)+abs(j-y)
                t.append((b,i,j))
    return t

def z(t):
    global shark_l,shark_b,shark_e
    f_x=t[1]
    f_y=t[2]
    s_q=deque([shark_l])
    while s_q:
        s=s_q.popleft()
        s_x=s[0]
        s_y=s[1]
        c=s[2]
        for i in range(4):
            nx=s_x+dx[i]
            ny=s_y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if nx==f_x and ny==f_y:
                    s_q=False
                    a[nx][ny]=0
                    shark_e+=1
                    if shark_e==shark_b:
                        shark_e=0
                        shark_b+=1
                    shark_l=[nx,ny,c+1]
                    break
                elif a[nx][ny]>shark_b:
                    continue
                s_q.append((nx,ny,c+1))
    
n=int(input())
a=[]
shark_b=2
shark_l=0
shark_e=0
r=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(n):
        if a[i][j]==9:
            shark_l=[i,j,0]

while True:
    t=check()
    if t==[]:
        break
    t.sort()
    f_q=deque(t)
    while f_q:
        z(f_q.popleft())

print(shark_l[2])


            
