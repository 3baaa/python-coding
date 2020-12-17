####다이나믹 프로그래밍####
'''
#다이나믹프로그래밍 문제4 (효율적인 화폐 구성)#
n,m=map(int,input().split())
a=[]
d=[10001]*(m+1)
for i in range(n):
  a.append(int(input()))

d[0]=0
for i in a:
  for j in range(i,m+1):
    if d[j-i]!=10001:
      d[j]=min(d[j],d[j-i]+1)

if d[m]!=10001:
  print(d[m])
else:
  print(-1)

####최단 경로####
import sys
input = sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)
distance=[INF]*(n+1)

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

def get_smallest_node():
  min_value = INF
  index=0
  for i in range(1,n+1):
    if distance[i]<min_value and not visited[i]:
      min_value=distance[i]
      index=i
  return index

def dijkstra(start):
  distance[start]=0
  visited[start]=True
  for j in graph[start]:
    distance[j[0]]=j[1]
  for i in range(n-1):
    now=get_smallest_node()
    visited[now]=True
    for j in graph[now]:
      cost=distance[now]+j[1]
      if cost < distance[j[0]]:
        distance[j[0]]=cost

dijkstra(start)

for i in range(1,n+1):
  if distance[i]==INF:
    print('INF')
  else:
    print(distance[i])
'''