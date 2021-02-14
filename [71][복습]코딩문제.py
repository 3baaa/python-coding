##자물쇠와 열쇠##
'''
#내가쓴 코드#
#(결과값은 나오나 정확성은 40.0 (밑의 주석부분으로 처리시 정확성 100) )#
import copy

def r(key):
    key2=copy.deepcopy(key)
    for i in range(len(key)):
        for j in range(len(key)):
            key[i][j]=key2[len(key)-j-1][i]
            
def ch(n,lock):
    for i in range(n,n+n):
        for j in range(n,n+n):
            if lock[i][j]==0 or lock[i][j]>1:
                return False
    return True

def kl(i,j,n,key,lock):
    print('i,j===',i,j)
    l1=0
    for k1 in range(i,i+n):
        l2=0
        for k2 in range(j,j+n):
            lock[k1][k2]+=key[l1][l2]
            l2+=1
        l1+=1
    return lock

def solution(key, lock):
    answer = False
    n=len(lock)
    a=[[0]*3*n for _ in range(3*n)]
    
    for i,v in enumerate(lock):
        for j,v2 in enumerate(v):
            a[i+n][j+n]=v2
    
    for k in range(4):
        for i in range(1,n+n):
            for j in range(1,n+n):
                lock=copy.deepcopy(a)
                lock=kl(i,j,n,key,lock)#kl(i,j,len(key),key,lock)하면 정확성 100
                if ch(n,lock):
                    return True
        r(key)
        
    return answer
'''
