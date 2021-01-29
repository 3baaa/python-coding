##퇴사##
'''
#내가쓴 코드#
#(결과값이 나온다)#
n=int(input())
a=[]
x=[]
for i in range(n):
  a.append(list(map(int,input().split())))

for i in range(1,n):
  if i+a[i][0]>n:
    x.append(i)
    continue
  r=0
  for j in range(0,i):
    if j not in x and j+a[j][0]<=i:
      r=max(r,a[j][1])
  a[i][1]+=r

r=0
for i in range(n):
  if i not in x:
    r=max(r,a[i][1])
print(r)

##병사 배치하기##
#답#
n=int(input())
array=list(map(int,input().split()))

dp=[1]*n

for i in range(1,n):
    for j in range(0,i):
        if array[j]>array[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))
'''
