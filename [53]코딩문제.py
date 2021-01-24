##안테나##
'''
#내가쓴 코드-1#
#(결과값이 나온다)#
n=int(input())
home=list(map(int,input().split()))
a=[0]*(max(home)+1)
for i in range(1,max(home)+1):
  for j in home:
    a[i]+=abs(i-j)
print(a.index(min(a[1:])))

##실패율##
#답#
def solution(N, stages):
    answer = []
    length=len(stages)
    
    for i in range(1,N+1):
        count=stages.count(i)
        if length==0:
            fail=0
        else:
            fail=count/length
        answer.append((i,fail))
        length-=count
    
    answer=sorted(answer,key=lambda t: t[1],reverse=True)
    answer=[i[0] for i in answer]
    return answer
'''
