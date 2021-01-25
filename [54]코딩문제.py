##카드 정렬하기##
'''
#내가쓴 코드#
#(결과값이 나온다)#
n=int(input())
a=[]
b=[]
r=[]
for i in range(n):
  a.append(int(input()))

#a.sort()를 해주면 더좋을것 같다

for i in range(n):
  if len(b)==2:
    n1=b.pop()
    n2=b.pop()
    r.append(n1+n2)
    b.append(n1+n2)
  b.append(a[i])
print(sum(r)+sum(b))

##정렬된 배열에서 특정 수의 개수 구하기##
#내가쓴 코드#
#(결과값이 나온다)#
from bisect import bisect_left,bisect_right

n,x=map(int,input().split())
a=list(map(int,input().split()))

print(bisect_right(a,x)-bisect_left(a,x))

##고정점 찾기##
#내가쓴 코드#
def biner(s,e):
  mid=(s+e)//2

  if s>e:
    return -1
  elif mid==a[mid]:
    return mid
  elif mid>a[mid]:
    return biner(mid+1,e)
  else:
    return biner(s,mid-1)

n=int(input())
a=list(map(int,input().split()))
print(biner(0,len(a)-1))

##공유기 설치##
#내가쓴 코드#
#(결과값이 나온다 하지만 잘못풀었다)# 
n,c=map(int,input().split())
a=[]
for i in range(n):
  a.append(int(input()))

a.sort()
r=0
for i in a[1:]:
  if i-a[0]>1:
    r=i
    break
print(r-a[0])

##공유기 설치##
#답#
n,c=list(map(int,input().split()))

array=[]
for _ in range(n):
  array.append(int(input()))

start=array[1]-array[0]
end=array[-1]-array[0]
result=0

while(start<=end):
  mid=(start+end)//2
  value=array[0]
  count=1
  for i in range(1,n):
    if array[i]>=value+mid:
      value=array[i]
      count+=1
  if count>=c:
    start=mid+1
    result=mid
  else:
    end=mid-1

print(result)
'''