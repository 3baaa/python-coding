##경쟁적 전염##
#내가쓴 코드#
#(결과값이 나온다)#
'''
from collections import deque

def bbb(s):
  t=0
  while check_zero(a):
    if t==s:
      return
    for i in range(1,k+1):
      if virus[i]:
        if not check_zero(a):
          return
        x,y=virus[i].popleft()
        for j in range(4):
          nx=x+dx[j]
          ny=y+dy[j]
          if nx<0 or nx>=n or ny<0 or ny>=n or a[nx][ny]!=0:
            continue
          a[nx][ny]=i
          virus[i].append((nx,ny))
    t+=1

def check_zero(a):
  for i in a:
    for j in i:
      if j==0:
        return True
  return False

n,k=map(int,input().split())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
a=[]
virus=[deque() for _ in range(k+1)]

for i in range(n):
  b=list(map(int,input().split()))
  for j,v in enumerate(b):
    if v!=0:
      virus[v].append((i,j))
  a.append(b)

s,x,y=map(int,input().split())

bbb(s)
print(a[x-1][y-1])

##괄호변환##
#답#
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if check_proper(u):
        answer = u + solution(v)

    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

##연산자 끼워 넣기##
#내가쓴 코드#
#(결과값이 잘나온다)#
from itertools import permutations

def four_rules_calculation(aa,bb,oper):
    if oper==0:
      return aa+bb
    elif oper==1:
      return aa-bb
    elif oper==2:
      return aa*bb
    elif oper==3:
      if aa<0:
        return -(-aa//bb)
      elif bb==0:
        return bb
      else:
        return aa//bb

def calculation():
  t=[]
  large_value=0
  small_value=int(1e9)
  for i in operation:
    l=0
    for j in a:
      t.append(j)
      if len(t)==2:
        bb=t.pop()
        aa=t.pop()
        t.append(four_rules_calculation(aa,bb,i[l]))
        l+=1
    r=t.pop()
    large_value=max(large_value,r)
    small_value=min(small_value,r)

  return large_value,small_value

n=int(input())
a=list(map(int,input().split()))
o=list(map(int,input().split()))
oper=[]
large_value=0
small_value=int(1e9)

for i,v in enumerate(o):
  for _ in range(v):
    oper.append(i)
operation=list(permutations(oper,n-1))
large_value,small_value=calculation()
print(large_value)
print(small_value)
'''