##실패율##
'''
#내가쓴 코드#
#(결과값이 나온다 정확성 100.0)#
def solution(N, stages):
    answer = []
    r=[]
    for i in range(N+1):
        r.append([i,0])
    for i in stages:
        if i!=N+1:
            r[i][1]+=1
    r=r[1:]
    l=len(stages)
    r2=[]
    print(r)
    for i in range(len(r)):
        t=r[i][1]
        if t==0.0:
            r[i][1]=0
        else:
            r[i][1]=r[i][1]/l
        l-=t
        r2.append(r[i])
    r2.sort(key=lambda x : x[1],reverse=True)
    for i in r2:
        answer.append(i[0])
    return answer
'''
