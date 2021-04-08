##모험가 길드
#내가쓴 코드
#결과값이 나온
n=int(input())
a=list(map(int,input().split()))

a.sort()
r=0
t=0
for i in a:
    t+=1
    if t==i:
        r+=1
        t=0

print(r)
    
