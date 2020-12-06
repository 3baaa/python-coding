'''
#번호 1097
a=[]
b=[]
c=[]
x=0
y=0
for i in range(19):
  c=list(map(int,input().split()))
  a.append(c)

n=int(input())

for i in range(n):
  c=list(map(int,input().split()))
  b.append(c)

for i in b:
  x=i[0]
  y=i[1]
  for j in range(19):
    if a[x-1][j]==0:
      a[x-1][j]=1
    else:
      a[x-1][j]=0
    pass
  for k in range(19):
    if a[k][y-1]==0:
      a[k][y-1]=1
    else:
      a[k][y-1]=0

for i in a:
  for j in i:
    print(j,end=' ')
  print()
#############################

#번호 1099
a=[]
x=1
y=1
c=0

for i in range(10):
  c=list(map(int,input().split()))
  a.append(c) 

while True:
  temp=a[x][y]
  a[x][y]=9
  if x==9 or y==9 or temp==2:
    break
  elif a[x][y+1]==1:
    if a[x+1][y]==1:
      break
    else:
      x+=1
  else:
    y+=1

for i in a:
  for j in i:
    print(j,end=' ')
  print()
'''
'''
with open('a.txt','r') as file:
  for i in file:
    a.append(list(map(int,i.strip().split())))
'''