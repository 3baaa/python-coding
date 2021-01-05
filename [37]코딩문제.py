##모험가 길드##
'''
#내가쓴 코드#
#(잘못쓴 코드 입력시 3\n2 3 3 했을때 1이나와야하는데 0이 나왔다)
n=int(input())
a=list(map(int,input().split()))

a.sort()
r=0
b=0
while a:
  now=a.pop(0)
  c=1
  d=True 
  for i in range(now-1):
    if len(a)==0:
      d=False
      break
    b=a.pop(0)
    c+=1
  if b<=c and d==True:
    r+=1

print(r)

#답#
n=int(input())
data=list(map(int,input().split()))
data.sort()

result=0

count=0

for i in data:
  count+=1
  if count>=i:
    result+=1
    count=0

print(result)

##곱하기 혹은 더하기##
#내가쓴 코드#
a=list(map(int,input()))
result=[]

for i in a:
  result.append(i)
  if len(result)==2:
    t1=result.pop()
    t2=result.pop()
    result.append(max(t2*t1,t2+t1))

print(result.pop())

##문자열 뒤집기##
#내가쓴 코드#
s=list(map(int,input()))

t1=0
t2=0
if s[0]==0:
  t1+=1
else:
  t2+=1
for i in range(len(s)-1):
  if s[i]!=s[i+1]:
    if s[i]==0:
      t1+=1
    else:
      t2+=1

print(min(t1,t2))

##만들수 없는 금액##
#답#
n=int(input())
data=list(map(int,input().split()))
data.sort()

target=1
for x in data:
  if target<x:
    break
  target+=x

print(target)
'''