##만들 수 없는 금액
#내가쓴 코드
#결과값이 나온다
n=int(input())
a=list(map(int,input().split()))

a.sort()
r=0
t=a[0]
if t>1:
    r=1
else:
    for i in a[1:]:
        if i>t+1:
            r=t+1
            break
        t+=i
print(r)
