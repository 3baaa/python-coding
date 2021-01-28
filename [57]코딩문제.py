##금광##
'''
#내가쓴 코드#
#(잘못쓴 코드)# 
T=int(input())
r=[]
nm=[]
a=[[] for _ in range(T)]
for i in range(T):
  n,m=map(int,input().split())
  nm.append((n,m))  
  t=list(map(int,input().split()))
  p=0
  for j in range(m,n*m+1,m):
    a[i].append(t[p:j])
    p=j

for i in range(T):
  s=0
  for j in range(nm[i][1]):
    p=0
    for k in range(nm[i][0]):
      t=a[i][k][j]
      p=max(t,p)
      print(t,end=' ')
    print()
    s+=p
  r.append(s)

print(r)

##금광##
#답#
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)

##정수 삼각형##
#내가쓴 코드#
n=int(input())
a=[]
for _ in range(n):
  a.append(list(map(int,input().split())))

for i in range(1,n):
  for j in range(len(a[i])):
    if j-1<0:
      left_up=0
    else:
      left_up=a[i-1][j-1]

    if j==len(a[i-1]):
      up=0
    else:
      up=a[i-1][j]

    a[i][j]+=max(left_up,up)

print(max(a[n-1]))
'''
