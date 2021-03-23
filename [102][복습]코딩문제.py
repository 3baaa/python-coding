##못생긴 수##
#내가쓴 코드#
#결과값이 나온다#
n = int(input())

t=1
z=1
while True:
    z+=1
    if z%2==0 or z%3==0 or z%5==0:
        t+=1
    if t==n:
        break
print(z)

