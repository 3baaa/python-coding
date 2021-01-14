##특정 거리의 도시##
'''
#내가쓴 코드#
#(결과값이 나온다)#
from collections import deque

def bb(z,k,s):
  start=(s,0)
  q=deque([start])
  result=[]
  while q:
    n,dist=q.popleft()
    for i in z[n]:
      distance[i]=min(distance[i],dist+1)
      if distance[i]==k:
        result.append(i)
      else:
        if distance[i]<k:
          q.append([i,distance[i]])
  return result

n,m,k,x=map(int,input().split())
distance=[1e9]*(n+1)

z=[[] for _ in range(n+1)]

for i in range(m):
  a,b=map(int,input().split())
  z[a].append(b)

result=bb(z,k,x)
result.sort()
if result:
  for i in result:
    print(i)
else:
  print(-1)
'''
##연구소##
#내가쓴 코드#
