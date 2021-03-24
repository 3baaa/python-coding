##편집 거리
#내가쓴 코드
#결과값이 나온다
a=input()
b=input()

r=0
if len(b)>len(a):
    a,b=b,a
ib=0
for i in range(len(a)):
    if a[i]==b[ib]:
        ib+=1
    else:
        if len(b)>=len(a)-r:
            ib+=1
        r+=1 
print(r)
