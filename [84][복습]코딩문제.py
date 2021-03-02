##고정점 찾기##
'''
#내가쓴 코드#
#(결과값이 나온다)#
def z(s,e):
    if s>e:
        return -1
    m=(s+e)//2
    if a[m]==m:
        return m
    elif a[m]<m:
        return z(m+1,e)
    else:
        return z(s,m-1)

n=int(input())
a=list(map(int,input().split()))

print(z(0,len(a)-1))
'''
