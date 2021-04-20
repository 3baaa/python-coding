##단어의 개수
#내가쓴 코드
#결과 = 맞았습니다!!
s=input().split()
print(len(s))
'''
#결과 = 시간 초과
s=input().split()
a=[]
r=0
for i in s:
    if i not in a:
        a.append(i)
        r+=1

print(r)
'''
