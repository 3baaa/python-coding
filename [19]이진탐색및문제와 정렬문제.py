####정렬문제####
'''
##두 배열의 원소 교체##
#내가쓴 코드#
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort()

for i in range(k):
  ##이걸써야된다##
  ##if a[i]<b[-(i+1)]
  a[i],b[-(i+1)]=b[-(i+1)],a[i]

print(sum(a))

####이진탐색####
##1##
def binary_s(array,target,start,end):
  if start>end:
    return None
  mid=(start+end)//2
  if array[mid]==target:
    return mid
  elif array[mid]>target:
    return binary_s(array,target,start,mid-1)
  else:
    return binary_s(array,target,mid+1,end)
  pass
n,target=list(map(int,input().split()))
array=list(map(int,input().split()))

result=binary_s(array,target,0,n-1)
if result==None:
  print("원소가 존재하지 않습니다.")
else:
  print(result+1)
##2##
def binary_s(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    if array[mid]==target:
      return mid
    elif array[mid]>target:
      end=mid-1
    else:
      start=mid+1
  return None
n,target=list(map(int,input().split()))
array=list(map(int,input().split()))

result=binary_s(array,target,0,n-1)
if result==None:
  print('원소가 존재하지 않습니다.')
else:
  print(result+1)

import sys
input_data=sys.stdin.readline().rstrip()

print(input_data)

##문제 1 (부품 찾기)##
#내가쓴 코드#
def b_s(a,target,start,end):
  mid=(start+end)//2
  if start>end:
    return 'no'
  elif a[mid]==target:
    return 'yes'
  elif target<a[mid]:
    return b_s(a,target,start,mid-1)
  else:
    return b_s(a,target,mid+1,end)

n=int(input())
a=list(map(int,input().split()))

m=int(input())
b=list(map(int,input().split()))

a.sort()
b.sort()

for i in b:
  print(b_s(a,i,0,len(a)-1),end=' ')

##문제 2 (떡볶이 떡 만들기)##
n,m=map(int,input().split())
a=list(map(int,input().split()))
c=[]

for i in range(max(a)):
  sum=0
  for j in a:
    sum+=(j-i)
  if sum==m:
    c.append(i)

print(c)
##########################
n,m=map(int,input().split())
a=list(map(int,input().split()))

def b_s(a,target,start,end):
  if start>end:
    return 'x'
  mid=(start+end)//2
  sum=0
  for i in range(len(a)):
    if a[i]>=mid:
      sum+=(a[i]-mid)
  if sum==target:
    return mid
  elif sum<target:
    return b_s(a,target,start,mid-1)
  else:
    return b_s(a,target,mid+1,end)


print(b_s(a,m,0,max(a)))
'''