##경쟁적 전염##
'''
#내가쓴 코드#
#(결과값이 나오나 밑의 주석을 넣어줘야한다)#
from collections import deque

def bb(s):
    q=deque(vv)
    t=0
    while q:
        v,x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                ##if a[nx][ny]==0:
                    a[nx][ny]=v
                    q.append([v,nx,ny])
        if k==v and q[0][0]!=v:
            t+=1
        if t==s:
            return
n,k=map(int,input().split())
vv=[]
a=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    t=list(map(int,input().split()))
    for j,v in enumerate(t):
        if v!=0:
            vv.append([v,i,j])
    a.append(t)
s,x,y=map(int,input().split())

vv.sort()
bb(s)
print(a[x-1][y-1])

##괄호변환##
#내가쓴 코드#
#(결과값은 나오나 정확도 32.0 하지만 밑의 주석부분으로 바꿔주면 정확도 100)#
def ch1(p):
    if p.count('(')==p.count(')'):
        return True
    return False

def ch2(p):
    a=[]
    for i in p:
        if i=='(':
            a.append('(')
        else:
            if a:
                a.pop()
            else:
                return False
    return True

def z(p):
    u=0
    v=0
    if p=='':
        return p
    for i in range(1,len(p)):
        if ch1(p[:i+1]):
            u=p[:i+1]
            v=p[i+1:]
            break
    if ch2(u):
        return u+z(v)
    else:
        r='('+v+')' ##r='('+z(v)+')'
        for i in u[1:-1]:
            if i=='(':
                r+=')'
            else:
                r+='('
        return r
            
        
        
def solution(p):
    answer=''
    if p=='' or ch2(p):
        return p
    return z(p)
'''
