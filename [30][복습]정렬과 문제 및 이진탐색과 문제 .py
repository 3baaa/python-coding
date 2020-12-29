####정렬####
'''
##계수정렬##
#내가쓴 코드#

array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

array2=[0]*(max(array)+1)

for i in array:
  array2[i]+=1

for i,v in enumerate(array2):
  for j in range(v):
    print(i,end=' ')
#답#
array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count=[0]*(max(array)+1)

for i in range(len(array)):
  count[array[i]]+=1

for i in range(len(count)):
  for j in range(count[i]):
    print(i,end=' ')

##sorted##
array=[7,5,9,0,3,1,6,2,4,8]

result=sorted(array)
print(result)

##sort##
array=[7,5,9,0,3,1,6,2,4,8]

array.sort()
print(array)

##key##
array=[('바',2),('사',5),('당',3)]

def setting(data):
  return data[1]

result=sorted(array,key=setting)
print(result)

##위에서 아래로(정렬문제1)##
#내가쓴 코드#
n=int(input())
array=[]

for i in range(n):
  array.append(int(input()))

array.sort(reverse=True)

for i in array:
  print(i,end=" ")

##성적이 낮은 순서로 학생 출력하기(정렬문제2)##
#내가쓴 코드#
n=int(input())
array=[]

for i in range(n):
  array.append(input().split())
  array[i][1]=int(array[i][1])

array.sort(key=lambda x: x[1])
for i in array:
  print(i[0],end=' ')

##두 배열의 원소 교체(정렬문제3))##
#내가쓴 코드#
n,k=map(int,input().split())
array=[]

for i in range(2):
  array.append(list(map(int,input().split())))

for i in range(k):
  a=min(array[0])
  b=max(array[1])
  array[0][array[0].index(a)],array[1][array[1].index(b)]=array[1][array[1].index(b)],array[0][array[0].index(a)]

print(sum(array[0]))

#답#
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i]<b[i]:
    a[i],b[i]=b[i],a[i]
  else:
    break

print(sum(a))

####이진탐색####
#내가쓴 코드1(재귀함수)#
n,t=list(map(int,input().split()))
array=list(map(int,input().split()))

def biner_search(s,e,t):
  m=(s+e)//2
  if s>e:
    return False
  elif array[m]==t:
    return m+1
  elif array[m]>t:
    return biner_search(s,m-1,t)
  else:
    return biner_search(m+1,e,t)

r=biner_search(0,len(array)-1,t)
if r==False:
  print('원소가 존재하지 않습니다')
else:
  print(r)

#내가쓴 코드2(반복문))#
n,t=list(map(int,input().split()))
array=list(map(int,input().split()))

def biner_search(s,e,t):
  while True:
    m=(s+e)//2
    if s>e:
      return False
    if array[m]==t:
      return m+1
    elif array[m]>t:
      e=m-1
    elif array[m]<t:
      s=m+1
      

r=biner_search(0,len(array)-1,t)
if r==False:
  print('원소가 존재하지 않습니다')
else:
  print(r)

##부품 찾기(이진 탐색문제1)##
#내가쓴 코드#
#(## no ##=코드를 잘못쓴부분 , ## yes ##=답보고 맞게쓴 부분)#
n=int(input())
array_n=list(map(int,input().split()))
array_n.sort()## yes ##
m=int(input())
array_m=list(map(int,input().split()))
r=[]

def biner_search(s,e,t):
  if s>e:
    return 'no'
  m=(s+e)//2
  if array_n[m]==t:
    return 'yes'
  elif array_n[m]>t:
    return biner_search(s,m-1,t)
  else:
    return biner_search(m+1,e,t)

for i in array_m:
  a=biner_search(0,len(array_n)-1,i)
  r.append(a)

for i in r:
  print(i,end=' ')

##떡볶이 떡 만들기(이진탐색문제2)##
#내가쓴 코드#
#(## no ##=코드를 잘못쓴부분 , ## yes ##=답보고 맞게쓴 부분)#
n,m=map(int,input().split())
array=list(map(int,input().split()))
array.sort()

def biner_search(s,e,t):
  sum=0
  while s<=e:
    sum=0
    m=(s+e)//2
    for i in array:
      if i>m:
        sum+=(i-m)
      #if i>array[m]:      ## no ##
      #  sum+=(i-array[m]) ## no ##
    #if sum==t:            ## no ##
    #  return array[m]     ## no ##
    if sum>t:
      s=m+1
    else:
      e=m-1
  return m                 ## yes ##
  #return array[m]         ## no  ##
r=biner_search(0,max(array),m)   ## yes ##
#r=biner_search(0,len(array)-1,m)## no  ##
print(r)

#답#
n,m=list(map(int,input().split(' ')))
array=list(map(int,input().split()))

start=0
end=max(array)

result=0
while(start<=end):
  total=0
  mid=(start+end)//2
  for x in array:
    if x>mid:
      total+=x-mid
  if total<m:
    end=mid-1
  else:
    result=mid
    start=mid+1

print(result)
'''