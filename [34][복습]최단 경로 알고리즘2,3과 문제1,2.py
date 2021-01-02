####최단 경로####
'''
##다익스트라 알고리즘2##
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[] for i in range(n+1)]
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
    print('INFINITY')
  else:
    print(distance[i])

##플로이드 워셜 알고리즘##
INF=int(1e9)

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
      print("INFINITY",end=" ")
    else:
      print(graph[a][b],end=" ")
  print()

##미래도시(최단경로 문제1)##
#내가쓴 코드#
INF=int(1e9)
n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
  a,b=map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1

x,k=map(int,input().split())

for i in range(1,n+1):
  graph[i][i]=0

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

r=graph[1][k]+graph[k][x]

if r<INF:
  print(r)
else:
  print(-1)

##전보(최단경로 문제2)##
#내가쓴 코드#
import heapq

INF=int(1e9)
n,m,c=map(int,input().split())

graph=[ [] * (n+1) for _ in range(n+1)]
distance=[INF]*(n+1)

for i in range(m):
  a,b,d=map(int,input().split())
  graph[a].append((b,d))

def dijkstra(a):
  q=[]
  s=a
  distance[s]=0
  heapq.heappush(q,(s,0))
  while q:
    now,dist=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      if distance[i[0]]>dist+i[1]:
        distance[i[0]]=dist+i[1]
        heapq.heappush(q,(i[0],dist+i[1]))
z=0
m=0
dijkstra(c)

for i in distance:
  if i==INF:
    continue
  else:
    if m<i:
      m=i
    if i!=0:
      z+=1
print(z,m)
'''