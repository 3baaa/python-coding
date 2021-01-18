##n과 m(4)##
'''
#내가쓴 코드#
#(결과값이 나온다)#
n,m=map(int,input().split())
v=[False]*(n+1)
a=[]

def dfs(z):
  if z==m:
    for i in a:
      print(i,end=' ')
    print()
    return
  
  for i in range(1,n+1):
    if not v[i]:
      a.append(i)
      dfs(z+1)
      v[i]=True
      a.pop()

      for j in range(i+1,n+1):
        v[j]=False

dfs(0)

##n과 m(5)##
#내가쓴 코드#
#(결과값이 나온다)#
def dfs(z):
  if z==m:
    for i in b:
      print(i,end=" ")
    print()
    return
  
  for i in range(n):
    if not v[i]:
      v[i]=True
      b.append(a[i])  
      dfs(z+1)
      b.pop()
      v[i]=False

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
v=[False]*n
a.sort()

dfs(0)

##n과 m(6)##
#내가쓴 코드#
#(결과값이 나온다)#
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
v=[False]*n

def dfs(z):
  if z==m:
    for i in b:
      print(i,end=' ')
    print()
    return
  for i in range(n):
    if not v[i]:
      v[i]=True
      b.append(a[i])
      dfs(z+1)
      b.pop()
      for j in range(i+1,n):
        v[j]=False

a.sort()
dfs(0)

##n과 m(7)##
#내가쓴 코드#
#(결과값이 나온다)#
def dfs(z):
  if z==m:
    for i in b:
      print(i,end=' ')
    print()
    return
  
  for i in range(n):
    b.append(a[i])
    dfs(z+1)
    b.pop()
    
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
v=[False]*n

a.sort()
dfs(0)

##n과 m(8)##
#내가쓴 코드#
#(결과값이 나온다)#
def dfs(z):
  if z==m:
    for i in b:
      print(i,end=' ')
    print()
    return
  
  for i in range(n):
    if not v[i]:
      b.append(a[i])
      dfs(z+1)
      v[i]=True
      b.pop()
      
      for j in range(i+1,n):
        v[j]=False

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
v=[False]*n

a.sort()
dfs(0)

##n과 m(9)##
#내가쓴 코드#
#(결과값은 나오지만 시간초과)#
def dfs(z):
  global r
  if z==m:
    if r.count(b)==0:
      r.append(b.copy())
    return
    
  
  for i in range(n):
    if not v[i]:
      b.append(a[i])
      v[i]=True
      dfs(z+1)
      b.pop()
      v[i]=False
  
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
r=[]
v=[False]*n

a.sort()
dfs(0)

for i in r:
  for j in i:
    print(j,end=' ')
  print()

##n과 m(9)##
#답#
def dfs(z):
  if z==m:
    for i in b:
      print(i,end=" ")
    print()
    return
    
  last=0
  for i in range(n):
    if not v[i] and last != a[i]:
      b.append(a[i])
      v[i]=True
      last=a[i]
      dfs(z+1)
      b.pop()
      v[i]=False
  
n,m=map(int,input().split())
a=list(map(int,input().split()))

b=[]
v=[False]*n

a.sort()
dfs(0)

##n과 m(10)##
#내가쓴 코드#
#(결과값은 나오지만 제출시 틀렸습니다)#
def dfs(z):
  if z==m:
    for i in b:
      print(i,end=" ")
    print()
    return
  
  last=0
  for i in range(n):
    if not v[i] and last!=a[i]:
      b.append(a[i])
      v[i]=True
      last=a[i]
      dfs(z+1)
      b.pop()
      
      for j in range(i+1,n):
        v[j]=False

n,m=map(int,input().split())
a=list(map(int,input().split()))
v=[False]*n
b=[]

a.sort()
dfs(0)

##n과 m(10)##
#답#
def dfs(z,idx):
  if z==m:
    for i in b:
      print(i,end=" ")
    print()
    return
  
  last=0
  for i in range(idx,n):
    if last!=a[i]:
      b.append(a[i])
      last=a[i]
      dfs(z+1,i+1)
      b.pop()

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]

a.sort()
dfs(0,0)

##n과 m(2)##
#답#
N, M = map(int, input().split())
visited = [False] * N
a = []

def dfs(z, idx):
    if z == M:
        print(' '.join(map(str, a)))
        return
    for i in range(idx, N):
        a.append(i+1)
        dfs(z+1, i+1)
        print(a)
dfs(0, 0)
'''