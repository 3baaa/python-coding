##치킨 배달##
'''
#내가쓴 코드#
#(결과값이 나오나 아마도 결점이 있는것 같다)#
n,m=map(int,input().split())
a=[[]]
h=[]
c=[]

for i in range(1,n+1):
    t=list(map(int,input().split()))
    for j,v in enumerate(t,start=1):
        if v==1:
            h.append([i,j])
        elif v==2:
            c.append([i,j])
    a.append(t)
    
r=[[] for _ in range(len(h))]
result=[]
r2=0

for i,v in enumerate(h):
    for j in c:
        r[i].append([abs(v[0]-j[0])+abs(v[1]-j[1]),j])
        r[i].sort()

count=0
p=[]
for i in r:
    if p!=i[0][1] and count<=m:
        count+=1
        p=i[0][1]

    if count>m:
        r2=int(1e9)
        for i in c:
            t=0
            for j in r:
                for k in j:
                    if k[1]==i:
                        t+=k[0]
            r2=min(r2,t)
        break
    else:
        r2+=i[0][0]
        
print(r2)
'''
