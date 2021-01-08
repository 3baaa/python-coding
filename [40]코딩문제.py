##자물쇠와 열쇠##
'''
#내가쓴 코드#
#(정확성 14.0)#
import copy
from collections import deque

def right(key):
    k=key
    for i,v in enumerate(k):
        for j in range(2,-1,-1):
            if v[j]==1:
                if j+1<=2:
                    k[i][j+1]=1
                k[i][j]=0
    return k

def left(key):
    k=key
    for i,v in enumerate(k):
        for j,v in enumerate(v):
            if v==1:
                if j-1>=0:
                    k[i][j-1]=1
                k[i][j]=0
    return k

def up(key):
    k=key
    for i in range(len(key)):
        for j in range(len(key)):
            if k[j][i]==1:
                if j-1>=0:
                    k[j-1][i]=1
                k[j][i]=0
    return k
def down(key):
    k=key
    for i in range(len(k)):
        for j in range(len(k)-1,-1,-1):
            if k[j][i]==1:
                if j+1<len(k):
                    k[j+1][i]=1
                k[j][i]=0
    return k

def r_rotation(array):
    z=2
    array2=copy.deepcopy(array)
    for i in array:
        for j,v in enumerate(i):
            array2[j][z]=v
        z-=1
    return array2

def c(a):
    b=0
    for i in a:
        for j in i:
            if j==1:
                b+=1
    return b

def b(key,lock):
    q=deque()
    q.append(key)
    lc=c(lock)
    m=[right,left,up,down,r_rotation]
    while q:
        k=q.popleft()
        for i in m:
            t=i(k)
            if c(t)<lc:
                continue
            elif t==lock:
                return True
            elif t==[[0,0,0],[0,0,0],[0,0,0]]:
                continue
            else:
                q.append(t)
    return False

def solution(key, lock):
    answer = True
    for i,v in enumerate(lock):
        for j,v in enumerate(lock):
            if v==0:
                lock[i][j]=1
            else:
                lock[i][j]=0
                
    answer=b(key,lock)
    return answer
'''