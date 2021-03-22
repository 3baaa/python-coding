##병사 배치하기
#내가쓴 코드#
#결과값이 나온다
n=int(input())
a=list(map(int,input().split()))
t=[[] for _ in range(n)]
t[0].append(a[0])
j=0
for i,v in enumerate(a[1:]):
    for k in t[j][:-1]:
        if v>k:
            j+=1
            break
    if len(t[j])>0 and t[j][-1]<v:
        t[j].pop()
    t[j].append(v)
    print('2=',t)
t=list(map(len,t))
print(n-max(t))
    
