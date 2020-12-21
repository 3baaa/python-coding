####다익스트라####
'''
import heapq
import sys
input = sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start = int(input())

graph=[[]for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
  if distance[i]==INF:
    print("INFINITY")
  else:
    print(distance[i])

####플로이드 워셜####
INF =int(1e9)

n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a][b]=c

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b]==INF:
      print('INFINITY',end=' ')
    else:
      print(graph[a][b],end=' ')
  print()

####문제 1(미래 도시))####
##내가쓴 코드##
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  graph[i][i]=0

for _ in range(m):
  a,b=map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1

x,k=map(int,input().split())

for l in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][l]+graph[l][j])
  
if graph[1][k]== INF or graph[k][x]==INF:
  print(-1)
else:
  print(graph[1][k]+graph[k][x])

####문제 2(전보)####
##내가쓴 코드##
import sys,heapq
input=sys.stdin.readline
INF=int(1e9)
q=[]

n,m,c=map(int,input().split())
distance=[INF for _ in range(n+1)]
graph=[[] for _ in range(n+1)]
for _ in range(m):
  x,y,z=map(int,input().split())
  graph[x].append((z,y))

distance[c]=0
heapq.heappush(q,(0,c))
while q:
  dist,a=heapq.heappop(q)
  if distance[a]<dist:
    continue
  for i in graph[a]:
    z=i[0]+dist
    if distance[i[1]]>z:
      distance[i[1]]=z
      heapq.heappush(q,(z,i[1]))

distance.sort()
count=0
for i in distance:
  if i!=0 and i!=INF:
    count+=1
print(count,distance[-2])
'''