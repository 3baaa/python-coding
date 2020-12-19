####최단 경로####
##다익스트라 최단 경로 알고리즘1##
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

n , m=map(int,input().split())

start=int(input())
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)
distance=[INF]*(n+1)

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

def get_smallest_node():
  min_value=INF
  index=0
  for i in range(1,n+1):
    if min_value>distance[i] and not visited[i]:
      min_value=distance[i]
      index=i
  return index

def dijkstra(start):
  distance[start]=0
  visited[start]=True
  distance[start]=0
  for i in graph[start]:
    distance[i[0]]=i[1]
    
  for i in range(1,n+1):
    s=get_smallest_node()
    visited[s]=True
    for j in graph[s]:
      if distance[j[0]]>(distance[s]+j[1]):
        distance[j[0]]=(distance[s]+j[1])

dijkstra(start)

for i in range(1,n+1):
  if distance[i]==INF:
    print('INF')
  else:
    print(distance[i])

import heapq
def heapsort(i):
  h=[]
  result=[]
  for v in i:
    heapq.heappush(h,v)
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result
result=heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

##다익스트라 최단 경로 알고리즘2##
import heapq
import sys
input = sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
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
'''