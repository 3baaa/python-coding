##미로탈출(dfs와 bfs문제2)##
'''
#내가쓴 코드#
#(## no ##=코드를 잘못쓴부분 , ## yes ##=답보고 맞게쓴 부분)#
from collections import deque
n,m=map(int,input().split())
a=[]

for i in range(n):
  a.append(list(map(int,input())))

def b(z):
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  queue=deque([z])
  #c=0 ## no ##
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<m:
        if a[nx][ny]==1:
          a[nx][ny]=a[x][y]+1 ## yes ##
          #c+=1 ## no ##
          #a[nx][ny]=c ## no ##
          queue.append((nx,ny))

b([0,0])

print(a[n-1][m-1])

####정렬####
##선택정렬##
#내가쓴 코드#
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)-1):
  m=10000
  for j in range(i,len(array)):
    if m>array[j]:
      m=array[j]
      m2=j
  array[i],array[m2]=array[m2],array[i]

print(array)

#답#
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index=i
  for j in range(i+1,len(array)):
    if array[min_index] > array[j]:
      min_index=j
  array[i],array[min_index]=array[min_index],array[i]

##삽입정렬##
#내가쓴 코드#
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
  z=array[i]
  for j in range(i-1,-1,-1):
    if z<array[j]:
      array[j+1]=array[j]
      array[j]=z

print(array)

#답#
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j]<array[j-1]:
      array[j],array[j-1]=array[j-1],array[j]
    else:
      break

print(array)

##퀵정렬##
#내가쓴 코드#
#(## no ##=코드를 잘못쓴부분 , ## yes ##=답보고 맞게쓴 부분)#
a=[7,5,9,0,3,1,6,2,4,8]

def quick(a,s,e):

  if s>=e: ## yes ##
    return ## yes ##
  #if s==e:## no ##
  #  return## no ##

  pivot=s
  left=s+1
  right=e
  
  while left<=right:## yes ##
  #while True:      ## no ##
    while left<=e and a[left] <= a[pivot]:## yes ##
      left+=1                             ## yes ##
    #for i in range(left,e+1):            ## no ##
    #  if a[pivot]<a[i]:                  ## no ##
    #    left=i                           ## no ##
    #    break                            ## no ##
    while right>s and a[right]>=a[pivot]: ## yes ##
      right-=1                            ## yes ##
    #for j in range(right,s,-1):          ## no ##
    #  if a[pivot]>a[right]:              ## no ##
    #    right=j                          ## no ##
    #    break                            ## no ##
    if left>right:
      a[pivot],a[right]=a[right],a[pivot] ## yes ##
      #break ## no ##
    else:
      a[right],a[left]=a[left],a[right]

  #a[pivot],a[right]=a[right],a[pivot]## no ##
  quick(a,s,right-1)
  quick(a,right+1,e)

quick(a,0,len(a)-1)
print(a)
'''