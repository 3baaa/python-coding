##여행 계획
#내가쓴 코드
#결과값이 나온다
def find_parent(n):
    if p[n]==n:
        return n
    p[n]=find_parent(p[n])
    return p[n]

def union_parent(a,b):
    a=find_parent(a)
    b=find_parent(b)
    if a<b:
        p[b]=p[a]
    else:
        p[a]=p[b]

n,m=map(int,input().split())
p=[]
for i in range(n):
    p.append(i)

for i in range(n):
    t=list(map(int,input().split()))
    for j in range(n):
        if t[j]==1:
            union_parent(i,j)

r=list(map(int,input().split()))
a=p[r[0]-1]
rr="YES"
for i in r[1:]:
    if a!=p[i-1]:
        rr="NO"
        break;
print(rr)
    
