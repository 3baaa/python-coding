##정수 삼각형##
#내가쓴 코드#
#결과값이 나온다#
n=int(input())
a=[]
for i in range(n):
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
