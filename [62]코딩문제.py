##여행 계획##
'''
#내가쓴 코드#
#(결과값이 나온다)#
def find_parent(i):
    if parent[i]!=i:
        parent[i]=find_parent(parent[i])
    return parent[i]

def union_parent(n1,n2):
    n1=find_parent(n1)
    n2=find_parent(n2)

    if n1>n2:
        parent[n1]=n2
    else:
        parent[n2]=n1
        
n,m=map(int,input().split())
a=[[] for _ in range(n+1)]
parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i
    
for i in range(1,n+1):
    t=list(map(int,input().split()))
    for j,v in enumerate(t,start=1):
        if v==1:
            a[i].append(j)
            
m2=list(map(int,input().split()))

for i in range(1,n+1):
    for j in a[i]:
        union_parent(i,j)

r="YES"
p=parent[m2[0]]
for i in m2[1:]:
    if p!=parent[i]:
        r="NO"
        break
    else:
        p=parent[i]
print(r)

##탑승구##
#답#
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

g=int(input())
p=int(input())
parent=[0]*(g+1)

for i in range(1,g+1):
    parent[i]=i

result=0
for _ in range(p):
    data=find_parent(parent,int(input()))
    if data==0:
        break
    union_parent(parent,data,data-1)
    result+=1

print(result)

##어두운 길##
#내가쓴 코드#
#(결과값이 나온다)#
def find_parent(i):
    if parent[i]!=i:
        parent[i]=find_parent(parent[i])
    return parent[i]

def union_parent(n1,n2):
    n1=find_parent(n1)
    n2=find_parent(n2)
    if n1<n2:
        parent[n2]=n1
    else:
        parent[n1]=n2
        
n,m=map(int,input().split())
a=[]
parent=[0]*n

for i in range(n):
    parent[i]=i
    
for _ in range(m):
    n1,n2,n=map(int,input().split())
    a.append([n,(n1,n2)])

a.sort()

r=0
for n,n12 in a:
    n1=n12[0]
    n2=n12[1]
    if find_parent(n1)!=find_parent(n2):
        union_parent(n1,n2)
    else:
        r+=n

print(r)
'''
