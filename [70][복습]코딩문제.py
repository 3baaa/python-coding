##럭키 스트레이트##
'''
#내가쓴 코드#
#(결과값이 나온다)#
n=input()
n=list(map(int,n))
length=len(n)//2

if sum(n[:length])==sum(n[length:]):
    print('LUCKY')
else:
    print('READY')

##문자열 재정렬##
#내가쓴 코드#
#(잘못쓴코드 = 숫자가 존재하지 않을때를 조건으로 못넣었다)#
s=input()
a=0
b=[]
c=''
for i in s:
    if '0'<=i<='9':
        a+=int(i)
    else:
        b.append(ord(i))
b.sort()
b=''.join(list(map(chr,b)))

## 맨밑의 'print(b+str(a))' 아닌 주석문장을 넣어야한다
##if a==0:
##    print(b)
##else:
##    print(b+str(a))
print(b+str(a))

##문자열 압축##
#내가쓴 코드#
#(결과값은 나오나 정확성은 62.0)#
def solution(s):
    answer = int(1e9)
    for i in range(1,len(s)//2+1):
        j=0
        p=''
        c=1
        r='' 
        while j+i<=len(s):
            n=s[j:j+i]
            if p==n:
                c+=1
            else:
                if c!=1:
                    r=r+str(c)+p
                    c=1
                else:
                    r+=p
                p=n
            j=j+i
        if j==len(s):
            if c!=1:
                r+=str(c)+n
            else:
                r+=n
        elif j<len(s):
            r+=n+s[j:]
        answer=min(answer,len(r))
    return answer

#답#
def solution(s):
    answer=len(s)
    for step in range(1,len(s)//2+1):
        compressed=''
        prev=s[0:step]
        count=1
        for j in range(step,len(s),step):
            if prev==s[j:j+step]:
                count+=1
            else:
                if count>=2:
                    compressed+=str(count)+prev
                else:
                    compressed+=prev
                prev=s[j:j+step]
                count=1
        if count>=2:
            compressed+=str(count)+prev
        else:
            compressed+=prev
        answer=min(answer,len(compressed))
    return answer
'''
