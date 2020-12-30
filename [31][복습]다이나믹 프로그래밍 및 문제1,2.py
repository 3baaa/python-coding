####다이나믹 프로그래밍####
'''
##피보나치수열1##
d=[0]*100

def fibo(x):
  if x==1 or x==2:
    return 1
  if d[x]!=0:
    return d[x]
  d[x]=fibo(x-1)+fibo(x-2)
  return d[x]

print(fibo(99))

##피보나치수열2##
d=[0]*100

d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
  d[i]=d[i-1]+d[i-2]

print(d[n])

##1로 만들기(다이나믹 프로그래밍 문제1)##
#내가쓴 코드#
(틀린코드 29를 입력했을때 정답은 5인데 입력시 3이 출력)
x=int(input())
c=0

while x!=1:
  while x%5!=0 and x%3!=0 and x%2!=0:
    print('1',x,c)
    x-=1
    c+=1
    print('2',x,c)
  a=x//5
  b=x//3
  c=x//2
  x=min(a,b,c)
  c+=1

print(c)

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

##개미전사(다이나믹 프로그래밍 문제2)##
#내가쓴 코드#
n=int(input())
k=list(map(int,input().split()))

d=[0]*(n+1)
m=0
d[0]=k[0]
d[1]=k[1]
d[2]=k[2]+k[0]
for  i in range(3,n):
    d[i]=k[i]+max(d[i-2],d[i-3])
    
r=max(d[n-2],d[n-1])
print(r)

#답#
n=int(input())

array=list(map(int,input().split()))

d=[0]*100

d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
  d[i]=max(d[i-1],d[i-2]+array[i])

print(d[n-1])
'''