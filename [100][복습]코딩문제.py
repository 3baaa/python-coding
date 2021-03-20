##퇴사##
#내가쓴코드#
#결과값이 나온다#
import copy
n=int(input())
a=[]*n

for _ in range(n):
    a.append(list(map(int,input().split())))

b=copy.deepcopy(a)
r=0

for i in range(n):
    t=i+a[i][0]
    if t<n:
        for j in range(t,n):
            if j+a[j][0]>n:
                continue
            b[j][1]=max(b[j][1],b[i][1]+a[j][1])
            r=max(r,b[j][1])
print(r)
