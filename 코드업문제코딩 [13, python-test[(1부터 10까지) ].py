#재귀 함수
'''
#문제 1901
def a(n):
  if n==0:
    return
  a(n-1)
  print(n)

n=int(input())
a(n)

#문제 1902
def a(n):
  if n==0:
    return
  print(n)
  a(n-1)
n=int(input())
a(n)

#문제 1903
def z(a,b):
  if a>b:
    return
  elif a%2!=0:
    print(a,end=' ')
  z(a+1,b)
a,b=map(int,input().split())
z(a,b)
'''
#문제 1904
'''
파이썬에서 maximum recursion depth exceeded in comparison 에러가 발생하는 경우

1. 원인
파이썬에서는 재귀 호출 횟수를 제한하고 있다.

2. 어떤 상황에서 일어나는가?
default값으로 설정되어 있는 재귀 호출 횟수(약 1000번?)을 넘어서면 에러가 발생한다.

3. 어떻게 해결하는가?
재귀 호출 횟수를 늘려주면 된다.

import sys
sys.setrecursionlimit(10**7) 처럼, 임의로 호출 횟수를 늘려주자.

출처: https://juhee-maeng.tistory.com/31 [BIU]
'''
'''
import sys
sys.setrecursionlimit(10**7)
def a(n):
  if n==0:
    return 0
  return n+a(n-1)
n=int(input())
print(a(n))
'''
'''
#가우스 공식으로도 된다
#https://m.blog.naver.com/PostView.nhn?blogId=a4gkyum&logNo=150181356024&proxyReferer=https:%2F%2Fwww.google.com%2F
def a(n):
  if n==0:
    return 0
  return ((1+n)*(n))//2
n=int(input())
print(a(n))

#문제 1912
def a(n):
  if n==1:
    return 1
  return n*a(n-1)
n=int(input())
print(a(n))

#문제 1915
def a(n):
  if n<=1:
    return n
  return a(n-1)+a(n-2)
n=int(input())
print(a(n))

#문제 1920
z=[]
def a(n):
  z.insert(0,str(n%2))
  if n//2==0:
    return
  a(n//2)
  
n=int(input())
a(n)
print(''.join(z))

#문제 1928
def a(n):
  if n==1:
    return
  elif n%2==0:
    print(n//2)
    a(n//2)
  else:
    print(3*n+1)
    a(3*n+1)
n=int(input())
print(n)
a(n)

#문제 1929
def a(n):
  if n==1:
    return
  elif n%2==0:
    a(n//2)
    print(n//2)
  else:
    a(3*n+1)
    print(3*n+1)
n=int(input())
a(n)
print(n)

#문제 1953
def a(n):
  if n==0:
    return
  a(n-1)
  print('*'*n)
n=int(input())
a(n)

#문제 3702
#내가쓴답
z=[[0]*50 for _ in range(50)]
def a(r,c):
  if r==1 or c==1:
    return 1
  elif z[r][c]!=0:
    return z[r][c]
  else:
    z[r][c-1]=a(r,c-1)
    z[r-1][c]=a(r-1,c)
  return a(r,c-1)+a(r-1,c)
r,c=map(int,input().split())
print(a(r,c)%100000000)

#답안지
z=[[0]*50 for _ in range(50)]
def a(r,c):
  if r==1 or c==1:
    return 1
  elif z[r][c]!=0:
    return z[r][c]
  z[r][c]=(a(r,c-1)+a(r-1,c))%100000000
  return z[r][c]
r,c=map(int,input().split())
print(a(r,c))

#문제 3704
#못풀어서 검색을 통해 해결
z=[0]*100001

def a(n):
  if n<0:
    return 0
  elif n==0:
    return 1
  else:
    if z[n]!=0:
      return z[n]
    else:
      z[n]=(a(n-2)+a(n-1)+a(n-3))%1000
      return z[n]

print(a(5))
'''