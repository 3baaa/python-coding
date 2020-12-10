#그리디
'''
#예시
n=1260
count=0

array=[500,100,50,10]

for coin in array:
  count += n // coin
  n %= coin

print(count)
'''
#### 문제1(그리디) ####
'''
## 1 나의 코드 ##
n,m,k=list(map(int,input().split()))
a=list(map(int,input().split()))
b=[0]*n
sum=0
a.sort()
while m>0:
  big=max(a)
  a_i=a.index(big)
  if a.count(big)>1 and k>1:
    a=a[a_i:]
    b=[0]*len(a)
    i=0
    j=0
    print(a)
    while m>0:
      if b[i]==k:
        b[i]=0
        i+=1
        i=i%len(a)
      sum+=a[i]
      m-=1
      b[i]+=1
  else:
    if b[a_i]==k:
      b[a_i]=0
      big=max(a[:a_i])
      a_i=a.index(big)
    sum+=big
    b[a_i]+=1
    m-=1

print(sum)
'''
'''
## 2 나의 코드 ##
n,m,k=list(map(int,input().split()))
a=list(map(int,input().split()))
b=[0]*n
sum=0
a.sort()
while m>0:
  big=max(a)
  a_i=a.index(big)

  if a.count(big)>1 and k>1:
    i=0
    l=len(a[a_i:])
    while m>0:
      if b[a_i+i]==k:
        b[a_i+i]=0
        i+=1
        i=i%l
      print(a[a_i+i],a_i+i,b[a_i+i])
      sum+=a[a_i+i]
      m-=1
      b[a_i+i]+=1
  else:
    if b[a_i]==k:
      b[a_i]=0
      big=max(a[:a_i])
      a_i=a.index(big)
  sum+=big
  b[a_i]+=1
  m-=1

print(sum)
'''
## 답 ##
n,m,k=map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

z=0

result = 0
while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1
  
print(result)