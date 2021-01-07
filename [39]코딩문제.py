##럭키 스트레이트##
'''
#내가쓴 코드#
n=input()

b=len(n)//2
s1=sum(map(int,n[0:b]))
s2=sum(map(int,n[b:]))
if s1==s2:
  print('LUCKY')
else:
  print('READY')

##문자열 재정렬##
#내가쓴 코드#
s=input()
sum=0
r=''
s=sorted(map(ord,s))
for i in s:
  if i>ord('9'):
    r+=chr(i)
  else:
    sum+=int(chr(i))
print(r+str(sum))

##문자열 압축##
#내가쓴 코드#
def solution(s):
    answer=0
    r=[0]*(len(s)//2+1)

    for i in range(1,len(s)//2+1):
        t=s[0:i]
        n=1
        for j in range(i,len(s),i):
            if t!=s[j:j+i]:
                if n!=1:
                    r[i]+=(i+1)
                else:
                    r[i]+=i
                t=s[j:j+i]
                n=1
            else:
                n+=1
        if j+i==len(s):
            if n!=1:
                r[i]+=(i+1)
            else:
                r[i]+=i
        elif j+i>len(s):
            r[i]+=len(s)-j
    answer=min(r[1:])
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