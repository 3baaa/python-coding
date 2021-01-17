##n과 m(1)##
'''
#답#
def d(z):
  if z==m:
    for i in a:
      print(i,end=" ")
    print()
    return

  for i in range(1,n+1):
    if not v[i]:
      a.append(i)
      v[i]=True
      b(z+1)
      a.pop()
      v[i]=False

n,m=map(int,input().split())
v=[False]*(n+1)
a=[]

b(0)

##n과 m(2)##
#답#
N, M = map(int, input().split())
visited = [False]*(N+1)
arr = []

def dfs(cnt):
  if cnt == M:
    for i in arr:
      print(i,end=' ')
    print()
    return
  
  for i in range(1,N+1):
    if not visited[i]:
      visited[i] = True
      arr.append(i)
      dfs(cnt+1)
      arr.pop()

      for j in range(i+1, N+1):
        visited[j] = False

dfs(0)

##n과 m(3)##
#내가쓴 코드#
n,m=map(int,input().split())
a=[]

def dfs(z):
  if z==m:
    for i in a:
      print(i,end=" ")
    print()
    return
  
  for i in range(1,n+1):
    a.append(i)
    dfs(z+1)
    a.pop()

dfs(0)
'''
