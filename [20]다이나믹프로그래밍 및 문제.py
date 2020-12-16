####다이나믹 프로그래밍####
'''
def fibo(x):
  if x==1 or x==2:
    return 1
  return fibo(x-1)+fibo(x-2)

print(fibo(4))

d=[0]*100

def fibo(x):
  if x==1 or x==2:
    return 1
  if d[x]!=0:
    return d[x]
  d[x]=fibo(x-1)+fibo(x-2)
  return d[x]

print(fibo(99))

d=[0]*100

d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
  d[i]=d[i-1]+d[i-2]

print(d[n])
## 다이나믹 프로그래밍 문제 1 (1로만들기) ##
#내가쓴 코드#
def d(x,a):
  c=0
  while True:
    if x%3!=0:
      x=-1
      
    while True:
      if x%5!=0:
        if a
        x-1
      else:
        x%=5
        c+=1
        break
    
    

  return c
x=int(input())
d(x)

#답#
x=int(input())

d=[0]*30001

for i in range(2,x+1):
  d[i]=d[i-1]+1
  if i%2==0:
    d[i]=min(d[i],d[i//2]+1)
  if i%3==0:
    d[i]=min(d[i],d[i//3]+1)
  if i%5==0:
    d[i]=min(d[i],d[i//5]+1)

print(d[x])
##다이나믹 프로그래밍 문제 2 (개미 전사) ##
#내가쓴 코드#
N=int(input())
K=list(map(int,input().split()))
a=[0]*N
sum=0
max=0
n=1
for i in range(0,N-1):

#답#
n=int(input())
array=list(map(int,input().split()))

d=[0]*100

d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
  d[i]=max(d[i-1],d[i-2]+array[i])

print(d[n-1])

##다이나믹 프로그래밍 문제 3 (바닥 공사) ##
#내가쓴 코드#
N=int(input())
c=[0]*N
c[1]=1
for i in range(2,N):
  c[i]=c[i-1]+c[i-2]*2

print(c[N-1]%796796)

#답#
n=int(input())

d=[0]*1001

d[1]=1
d[2]=3
for i in range(3,n+1):
  d[i]=(d[i-1]+2*d[i-2])%796796

print(d[n])

##다이니믹 프로그래밍 문제 4 (효율적인 화폐 구성)##
#내가쓴 코드#
n,m=map(int,input().split())
a=[]
d=[0]*100
for i in range(n):
  a.append(int(input()))

for i in range(m+1):
  for j in a:
    if i%j==0 and i<=max(a):
      while True:
        k=i//j
        if k==0:
          break
        elif k<j:
          d[i]=0
        else:
          d[i]+=1
    elif i%j==0:
      d[i]=d[i//j]*j

for i in d:
  print(i,end=' ')

#답#
n,m=map(int,input().split())

array=[]
for i in range(n):
  array.append(int(input()))

d=[10001]*(m+1)

d[0]=0
for i in range(n):
  for j in range(array[i],m+1):
    print(j,array[i],'/',i,'/',j-array[i])
    if d[j-array[i]]!=10001:
      print(d[j],d[j-array[i]]+1)
      d[j]=min(d[j],d[j-array[i]]+1)

if d[m]==10001:
  print(-1)
else:
  print(d[m])
'''