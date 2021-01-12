##치킨 배달##
'''
#내가쓴 코드#
#(결과값이 나온다)#
n,m=map(int,input().split())

a=[]
home=[]
chicken=[]

for i in range(n):
  a.append(list(map(int,input().split())))

for i,v in enumerate(a):
  for j,v in enumerate(v):
    if v==1:
      home.append((i,j))
    elif v==2:
      chicken.append((i,j))

result=[[0,[]] for _ in range(len(chicken))]
result2=[]
result3=0

for i,v1 in enumerate(chicken):
  r1,c1=v1
  for j,v2 in enumerate(home):
    r2,c2=v2
    t=abs(r1-r2)+abs(c1-c2)
    result[i][0]+=t
    result[i][1].append(t)
  result[i].append(v1)

result.sort()

t=[0]
c=0
for i in range(m):
  result2.append(result[i][2])

for i,v1 in enumerate(home):
  r1,c1=v1
  z=100
  for j,v2 in enumerate(result2):
    r2,c2=v2
    t=abs(r1-r2)+abs(c1-c2)
    z=min(z,t)
  result3+=z

print(result3)

#답#
from itertools import combinations

n,m=map(int,input().split())
chicken,house=[],[]

for r in range(n):
  data = list(map(int,input().split()))
  for c in range(n):
    if data[c]==1:
      house.append((r,c))
    elif data[c]==2:
      chicken.append((r,c))

candidates=list(combinations(chicken,m))

def get_sum(candidate):
  result=0
  for hx,hy in house:
    temp=1e9
    for cx,cy in candidate:
      temp = min(temp,abs(hx-cx)+abs(hy-cy))
    result+=temp
  return result

result=1e9
for candidate in candidates:
  result=min(result,get_sum(candidate))

print(result)
'''