##카드 정렬하기##
'''
#내가쓴 코드#
#(결과값이 나온다)#
def z():
    r=0
    for i in a:
        b.append(i)
        if len(b)==2:
            b.append(b.pop()+b.pop())
            r+=b[0]
    return r

n=int(input())
a=[]
b=[]
for _ in range(n):
    a.append(int(input()))

a.sort()

print(z())

##정렬된 배열에서 특정 수의 개수 구하기##
#내가쓴 코드#
#(결과값이 나온다)#
from bisect import bisect_right,bisect_left

n,x=map(int,input().split())
a=list(map(int,input().split()))

r1=bisect_right(a,x)
r2=bisect_left(a,x)
if r1==r2:
    print(-1)
else:
    print(r1-r2)
'''
