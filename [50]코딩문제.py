##n과 m(11)##
'''
#내가쓴 코드#
#(결과값이 나온다 제출시 통과)#
def dfs(z):
  if z==m:
    for i in b:
      print(i,end=" ")
    print()
    return

  last=0
  for i in range(n):
    if last!=a[i]:
      b.append(a[i])
      dfs(z+1)
      last=b.pop()

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]

a.sort()
dfs(0)

##n과 m(12)##
#내가쓴 코드#
#(결과값이 나온다 제출시 통과)#
def dfs(z,z1):
  if z==m:
    for i in b:
      print(i,end=" ")
    print()
    return
  
  last=0
  for i in range(z1,n):
    if last!=a[i]:
      b.append(a[i])
      dfs(z+1,i)
      last=b.pop()

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]

a.sort()
dfs(0,0)

##연산자 끼워 넣기##
#(47일차 풀었던 코드의 다른 풀이)#
#답#
n=int(input())
data=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

min_value=int(1e9)
max_value=int(-1e9)

def dfs(i,now):
  global min_value,max_value,add,sub,mul,div

  if i==n:
    min_value=min(min_value,now)
    max_value=max(max_value,now)
  else:
    if add>0:
      add-=1
      dfs(i+1,now+data[i])
      add+=1
    if sub>0:
      sub-=1
      dfs(i+1,now-data[i])
      sub+=1
    if mul>0:
      mul-=1
      dfs(i+1,now*data[i])
      mul+=1
    if div>0:
      div-=1
      dfs(i+1,int(now/data[i]))
      div+=1

dfs(1,data[0])

print(max_value)
print(min_value)
'''