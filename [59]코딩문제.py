##못생긴 수##
'''
#내가쓴 코드#
#(결과값이 나온다)#
n=int(input())
a=[1]
number=[2,3,5]
for i in range(1000):
    for j in number:
        t=a[i]*j
        if t not in a:
            a.append(t)
a.sort()   
print(a[n-1])

#답#
n=int(input())
ugly=[0]*n
ugly[0]=1

i2=i3=i5=0
next2,next3,next5=2,3,5

for l in range(1,n):
    ugly[l]=min(next2,next3,next5)
    if ugly[l]==next2:
        i2+=1
        next2=ugly[i2]*2
    if ugly[l]==next3:
        i3+=1
        next3=ugly[i3]*3
    if ugly[l]==next5:
        i5+=1
        next5=ugly[i5]*5

print(ugly[n-1])

##편집거리##
#답#
def edit_dist(str1,str2):
    n=len(str1)
    m=len(str2)

    dp=[[0] * (m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dp[i][0]=i
    for j in range(1,m+1):
        dp[0][j]=j

    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    return dp[n][m]

str1=input()
str2=input()
print(edit_dist(str1,str2))
'''
