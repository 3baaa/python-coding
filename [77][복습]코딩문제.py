##연산자 끼워 넣기##
'''
#내가쓴 코드#
#(결과값이 나온다)#
def ch(n1,n2,o):
    if o==0:
        return n1+n2
    elif o==1:
        return n1-n2
    elif o==2:
        return n1*n2
    else:
        if n1<0:
            return -((-n1)//n2)
        else:
            return n1//n2
        
def zz(oper,z,z2):
    global result1
    global result2
    if z==z2:
        nn=[]
        j=0
        for i in a:
            nn.append(i)
            if len(nn)==2:
                r=ch(nn.pop(0),nn.pop(0),oper[j])
                j+=1
                nn.append(r)
        t=nn.pop()
        result1=max(result1,t)
        result2=min(result2,t)
        return
    for i in range(4):
        if b[i]!=0:
            b[i]-=1
            oper.append(i)
            zz(oper,z+1,z2)
            oper.pop()
            b[i]+=1
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
result1=0
result2=int(1e9)
oper=[]
zz(oper,0,sum(b))
print(result1)
print(result2)

##감시 피하기##
#내가쓴 코드#
#(결과값이 나온다)#
def zz(b):
    if b==3:
        for i in T:
            for j in range(4):
                x,y=i
                while True:
                    nx=x+dx[j]
                    ny=y+dy[j]
                    if nx<0 or nx>=n or ny<0 or ny>=n or a[nx][ny]=='O':
                        break
                    if a[nx][ny]=='S':
                        return 'NO'
                    x,y=nx,ny
        return 'YES'
    for i in range(n):
        for j in range(n):
            if a[i][j]=='X':
                b+=1
                a[i][j]='O'
                if zz(b)=='YES':
                    return 'YES'
                a[i][j]='X'
                b-=1
    return 'NO'
n=int(input())
a=[]
T=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    a.append(input().split())
    for j in range(n):
        if a[i][j]=='T':
            T.append([i,j])
print(zz(0))
