##어두운 길
#내가쓴 코드
#결과값이 나온다
def find_p(n):
    if p[n]!=n:
        p[n]=find_p(p[n])
    return p[n]

def union_p(n1,n2):
    n1=find_p(n1)
    n2=find_p(n2)
    if n1>n2:
        p[n1]=p[n2]
    else:
        p[n2]=p[n1]
        
n,m=map(int,input().split())
p=[0]*n
a=[]
s=0
r=0
for i in range(n):
    p[i]=i

for _ in range(m):
    x,y,z=map(int,input().split())
    s+=z
    a.append((z,x,y))

a.sort()

for z,x,y in a:
    if find_p(x)!=find_p(y):
        union_p(x,y)
        r+=z
        
print(s-r)
