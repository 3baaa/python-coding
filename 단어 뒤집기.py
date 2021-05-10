##단어 뒤집기
#내가쓴 코드
#결과 = 맞았습니다!!
tc = int(input())
for i in range(tc):
    r=""
    a=[]
    str=input()
    for i in str:
        if i==" ":
            for j in a[::-1]:
                r+=j
            r+=" "
            a=[]
        else:
            a.append(i)
            
    for i in a[::-1]:
        r+=i
    print(r)
    
