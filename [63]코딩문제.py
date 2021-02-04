##행성 터널##
'''
#내가쓴 코드#
#(잘못쓴 코드)#
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
        
N=int(input())
a=[]
a2=[]
parent=[0]*N

for i in range(N):
    parent[i]=i
    
for i in range(N):
    a.append(list(map(int,input().split())))
    x1,y1,z1=a[i]
    for j in range(i-1,-1,-1):
        x2,y2,z2=a[j]
        a2.append([min(abs(x1-x2),abs(y1-x2),abs(z1-z2)),i,j])


a2.sort()
c=0
r=0
for n1,n2,n3 in a2:
    if find_parent(n2)!=find_parent(n3):
        union_parent(n2,n3)
        r+=n1

print(r)

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

n=int(input())
parent=[0]*(n+1)

edges=[]
result=0

for i in range(1,n+1):
    parent[i]=i

x=[]
y=[]
z=[]

for i in range(1,n+1):
    data=list(map(int,input().split()))
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))

x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))

edges.sort()

for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        
print(result)
'''
    
