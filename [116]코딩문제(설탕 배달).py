##설탕 배달
#내가쓴 코드
#결과 = 맞았습니다!!
n=int(input())
r=0
t=0
n1=(n//5)
n2=0

while True:
    t=n-((5*n1)+(3*n2))
    if t<=0:
        break
    if t<3 and n1>0:
        n1-=1
    n2+=1

if t<0:
    print(-1)
else:
    print(n1+n2)
'''
n1=(n//5)
n2=0
while True:
    print("n1=",n1,"n2=",n2)
    t=n-((5*n1)+(3*n2))
    if t==3:
        n2+=1
        break
    elif n-((5*n1)+(3*n2))<3:
        n1-=1
        n2+=1
    if n1==0 and n2==0:
        break
    print("n1=",n1,"n2=",n2)
'''
'''
if n>=5 and n%5>=3:
    print(111111)
    t=n%5
    r+=(n//5)
    r+=(t//3)
elif n%3==0:
    print(222222)
    r+=(n//3)
else:
    r=-1
'''
'''
while i<2:
    t+=a[i]
    r+=1
    print("n=",n,"t=",t,"i=",i,"r=",r)
    if n-t<a[i]:
        #t-=a[i]
        #r-=1
        i+=1
'''
'''
r+=(n//5)
t=n%5
r+=(t//3)
t=t%3
if t!=0:
    r=0
    r+=(n//3)
    t=n%3
    r+=(t//5)
    t=t%5
'''
