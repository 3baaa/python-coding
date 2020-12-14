####정렬####
'''
#선택정렬#
a=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(a)):
  min_i=i
  for j in range(i+1,len(a)):
    if a[min_i]>a[j]:
      min_i=j
  a[i],a[min_i]=a[min_i],a[i]
print(a)

#삽입정렬#
a=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(a)):
  for j in range(i,0,-1):
    if a[j-1]>a[j]:
      a[j-1],a[j]=a[j],a[j-1]
    else:
      break

print('a=',a)

#퀵정렬#
a=[7,5,9,0,3,1,6,2,4,8]

def quick(array,start,end):
  if start>=end:
    return
  pivot=start
  left=start+1
  right=end
  while left <= right:
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right:
      array[right],array[pivot] = array[pivot],array[right]
    else:
      array[left],array[right] = array[right],array[left]
  quick(array,start,right-1)
  quick(array,right+1,end)

quick(a,0,len(a)-1)
print(a)

#계수정렬#
a=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

b=[0]*(max(a)+1)

for i in range(len(a)):
  b[a[i]]+=1
for i in range(len(b)):
  for j in range(b[i]):
    print(i,end=' ')

#for i in a:
#  b[i]+=1

#for i in range(len(b)):
#  for j in range(b[i]):
#    print(i,end=' ')

####정렬문제####
##문제 1 (위에서 아래로)##
#내가쓴 코드#
n=int(input())
a=[]

for i in range(n):
  a.append(int(input()))

a.sort()
reversed(a)
for i in a:
  print(i,end=' ')

##문제 1 (성적이 낮은 순서로 학생 출력하기)##
#내가쓴 코드
n=int(input())
a={}

for i in range(n):
  b=input().split()
  a[b[0]]=int(b[1])

c=sorted(a,key=lambda x:x[1],reverse=True)

for i in range(n):
  print(c[i],end=' ')
'''
