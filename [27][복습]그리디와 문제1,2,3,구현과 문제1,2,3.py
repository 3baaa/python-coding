####그리디####
'''
n=1260
count=0

coin_types=[500,100,50,10]

for coin in coin_types:
  count += n // coin
  n%=coin

print(count)

##그리디 문제1(큰 수의 법칙)##
#내가쓴 답#
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
sum=0

a.sort()
z=0

for i in range(m):
  if z==k:
    z=0
    sum+=a[-2]
    continue
  z+=1
  sum+=a[-1]

print(sum)

#답#
n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

count = int(m/(k+1))*k
count += m % (k+1)

result = 0
result += (count)*first
result += (m-count)*second
print(result)

##그리디 문제2(숫자 카드 게임)##
#내가쓴 코드#
n,m=map(int,input().split())
a=[]
m_n=10000

for i in range(n):
  a.append(list(map(int,input().split())))

print(max(map(min,a)))

##그리디 문제3(1이 될 때까지)##
#내가쓴 코드#
n,k=map(int,input().split())
c=0

while n!=1:
  if n%k != 0:
    n-=1
    c+=1
  if n==1:
    break
  n//=k
  c+=1

print(c)

#답#
n,k=map(int,input().split())
result=0

while True:
  target=(n//k)*k
  result+=(n-target)
  n=target
  if n<k:
    break
  result+=1
  n//=k

result+=(n-1)
print(result)

####구현####
##구현 문제1(상하좌우)##
#내가쓴 코드#
n=int(input())
a=input().split()

x=1
y=1
for i in a:
  if i=='R':
    dx=x+0
    dy=y+1
  elif i=='L':
    dx=x+0
    dy=y-1
  elif i=='U':
    dx=x-1
    dy=y+0
  else:
    dx=x+1
    dy=y+0
  if dx<1 or dx>n or dy<1 or dy>n:
    continue
  x=dx
  y=dy

print(x,y) 

##구현 문제2(시각)##
#내가쓴 코드#
n=int(input())
c=0
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) or '3' in str(j) or '3' in str(k):
        c+=1

print(c)

##구현 문제3(왕실의 나이트)##
#내가쓴 코드#
n=input()
x=int(n[1])
y=ord('a')-ord(n[0])+1
a=[(-1,2),(1,2),(-1,-2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
c=0
for i in a:
  dx=x+i[0]
  dy=y+i[1]
  if dx<1 or dx>8 or dy<1 or dy>8:
    continue
  c+=1
print(c)
'''