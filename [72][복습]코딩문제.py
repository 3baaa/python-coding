##뱀##
'''
#내가쓴 코드#
#(결과값이 나온다)#
from collections import deque

n=int(input())
n2=[[0]*(n+1) for _ in range(n+1)]
k=int(input())
for i in range(k):
    x,y=map(int,input().split())
    n2[x][y]=1
    
L=int(input())
L2=[]
for i in range(L):
    t=input().split()
    t[0]=int(t[0])
    L2.append(t)

snake=deque([[1,1]])
d=1
t=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
while True:
    t+=1
    x,y=snake[0]
    nx=x+dx[d]
    ny=y+dy[d]
    if nx>=1 and nx<=n and ny>=1 and ny<=n and [nx,ny] not in snake:
        if n2[nx][ny]==1:
            n2[nx][ny]=0
        else:
            snake.pop()
        snake.appendleft([nx,ny])
    else:
        break
    for x,c in L2:
        if x==t:
            if c=='L':
                d-=1
                if d==-1:
                    d=3
            else:
                d+=1
                if d==4:
                    d=0

print(t)

##기둥과 보 설치##
#내가쓴 코드#
#(결과값은 나오나 정확성은 4.8)#
def solution(n, build_frame):
    answer = []
    for i in build_frame:
        x,y,a,b=i
        if a==0 and (y<0 or y>=n or x<0 or x>n):
            continue
        elif a==1 and (y<0 or y>n or x<0 or x>=n):
            continue

        if b==1:
            if a==0:
                print(1)
                if y==0 or ([x,y-1,0] in answer) or ([x-1,y,1] in answer):
                    answer.append([x,y,0])
            else:
                if ([x,y-1,0] in answer) or ([x+1,y-1,0] in answer) or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                    answer.append([x,y,1])
        else:
            if a==0:
                if ([x+1,y+1,1] in answer and [x-1,y+1,1] in answer) or ([x-1,y+1,1] not in answer) and ([x,y+1,1] not in answer):
                    answer.remove([x,y,0])
            else:
                if ([x+1,y,0] not in answer) and ([x-1,y,1] not in answer and [x+1,y,1] not in answer):
                    answer.remove([x,y,1])
    answer.sort()
    return answer

#답#
def possible(answer):
    for x,y,stuff in answer:
        if stuff==0:
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff==1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer=[]
    for frame in build_frame:
        x,y,stuff,operate=frame
        if operate==0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        if operate==1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)
'''
