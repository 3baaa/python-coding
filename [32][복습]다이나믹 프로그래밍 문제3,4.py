####다이나믹 프로그래밍####
'''
##바닥공사(다이나믹 프로그래밍 문제3)##
#답#
n=int(input())

d=[0]*1001

d[1]=1
d[2]=3
for i in range(3,n+1):
  d[i]=(d[i-1]+2*d[i-2])%796796

print(d[n])

##효율적인 화폐 구성(다이나믹 프로그래밍 문제4)##
#내가쓴 코드#
n,m=map(int,input().split())
d=[0]*10001
array=[]
for i in range(n):
  array.append(int(input()))
  d[array[i]]=1

for i in range(min(array)+1,m+1):
  if d[i]==0:
    z=10001
    for j in range(len(array)):
      t=i-array[j]
      if t>=min(array) and d[t]!=0:
        if z>d[t]:
          z=d[t]+1
    if z!=10001:
      d[i]=z
if d[m]!=0:
  print(d[m])
else:
  print(-1)

#답#
n,m=map(int,input().split())
array=[]
for i in range(n):
  array.append(int(input()))

d=[10001]*(m+1)

d[0]=0
for i in range(n):
  for j in range(array[i],m+1):
    if d[j-array[i]]!=10001:
      d[j]=min(d[j],d[j-array[i]]+1)

if d[m]==10001:
  print(-1)
else:
  print(d[m])
'''