'''
#번호 1001
print('Hello')

#번호 1002
print('Hello World')

#번호 1003
print('Hello\nWorld')

#번호 1004
print('\'Hello\'')

#번호 1005
print('\"Hello World\"')

#번호 1006
print('\"!@#$%^&*()\"')

#번호 1007
print('\"C:\Download\he):
  print(chr(i),sep=" ")

#번호 1076
s=ord(input())
for i in range(ord('a'),s+1):
  print(chr(i),end=" ")

#번호 1071
a = input().split()
for i in a:
  if i=='0':
    break
  print(i)

#번호 1070
s=int(input())

if s==1 or s==2 or s==12:
  print('winter')
elif 3<=s<=5:
  print('spring')
elif 6<=s<=8:
  print('summer')
else:
  print('fall')

n=int(input())
sum=0

#번호 1080
for i in range(n+1):
  sum+=i
  if sum>=n:
    print(i)
    break

#번호 1081
a,b=map(int,input().split())

for i in range(1,a+1):
  for j in range(1,b+1):
    print(i,j)
'''
#번호
#print(int(input(),16))
'''
for i in range(1,16):
  #while True:
    
  print(str(hex(int('0xA',16)*i))[2:])
  if i>=10:
    i=chr(ord('A')+i%10)
  print('B *',i,'=','0')

#번호 1082
a = ord(input())
if not ord('A')<=a<=ord('F'):
  print('x')
else:
  a=chr(a)
  for i in range(1,16):
    if i>=10:
      i=chr(ord('A')+i%10)
      r=str(hex(int('0x'+i,16)*int('0x'+a,16)))[2:].upper()
    else :
      r=str(hex(i*int('0x'+a,16)))[2:].upper()
    print(f'{a}*{i}=',r)

#번호 1083
a=int(input())
for i in range(1,a+1):
  if i%3==0:
    print('X',end=' ')
  else:
    print(i,end=' ')

#번호 1084
a,b,c=map(int,input().split())
d=0

for i in range(a):
  for j in range(b):
    for k in range(c):
      print(i,j,k)
      d+=1
print(d)

#번호 1088
a = int(input())

for i in range(a+1):
  if i%3!=0:
    print(i,end=' ')

#번호 1089
a,d,n=map(int,input().split())
print(a+(d*(n-1)))

#번호 1090
a,r,n=map(int,input().split())
for i in range(1,n):
  a=a*r
print(a)

#번호 1091
a,m,d,n=map(int,input().split())
for i in range(1,n):
  a=a*m+d
print(a)

#번호 1092
a,b,c=map(int,input().split())
s=a*b*c
day=1
while day%a!=0 or day%b!=0 or day%c!=0:
  day+=1
print(day)

#번호 1093
n=int(input())
arr=list(map(int,input().split()))
for i in range(1,24):
  print(arr.count(i),end=' ')

#번호 1094
n=int(input())
k=list(map(int,input().split()))
k.reverse()
for i in k:
  print(i,end=' ')

#번호 1095
n=int(input())
k=list(map(int,input().split()))
print(min(k))

#번호 1096
n=int(input())
b=[[0]*19 for _ in range(19)]
for i in range(n):
  x,y=list(map(int,input().split()))
  b[x-1][y-1]=1

for i in b:
  for j in i:
    print(j,end=' ')
  print()
'''

