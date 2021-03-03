##공유기 설치##
'''
#내가쓴 코드#
#(잘못쓴코드)
def ch(s,e):
    
    print(z_r(0,2))
    print(z_l(2,4))

def z_r(s,e):
    if s>=e:
        return s
    m=(s+e)//2
    return z_r(m+1,e)

def z_l(s,e):
    if s>=e:
        return s
    m=(s+e)//2
    return z_l(s,m-1)

n,c=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
print(a)
r=[]
a.sort()
ch(0,len(a))

#답#
n,c=list(map(int,input().split(' ')))

array=[]
for _ in range(n):
    array.append(int(input()))

array.sort()

start = array[1]-array[0]
end = array[-1]-array[0]
result=0

while(start<=end):
    mid=(start+end)//2
    value=array[0]
    count=1

    for i in range(1,n):
        if array[i]>=value+mid:
            value=array[i]
            count+=1
    if count>=c:
        start = mid +1
        result=mid
    else:
        end = mid - 1

print(result)
'''
