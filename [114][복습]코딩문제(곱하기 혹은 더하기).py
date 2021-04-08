##곱하기 혹은 더하기
#내가쓴 코드
#결과값이 나온다
s=list(map(int,input()))

r=0
for i in s:
    if i==1 or i==0 or r==0:
        r+=i
    else:
        r*=i

print(r)
