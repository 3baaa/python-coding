##가사 검색##
'''
#내가쓴 코드#
#(결과값은 나오나 정확성 테스트 통과 + 효율성 테스트 3개 실패로 합계 55.0)##
from bisect import bisect_left,bisect_right
        
def solution(words, queries):
    answer=[]
    t1=[[] for _ in range(10001)]
    t2=[[] for _ in range(10001)]
    for i in words:
        l=len(i)
        t1[l].append(i)
        t1[l].sort()
        t2[l].append(i[::-1])
        t2[l].sort()
    for i,vi in enumerate(queries):
        t=0
        if vi[0]=='?':
            vi=vi[::-1]
            t=1
        l=len(vi)
        tl=vi.replace('?','a')
        tr=vi.replace('?','z')
        if t==1:
            answer.append(bisect_right(t2[l],tr)-bisect_left(t2[l],tl))
        else:
            answer.append(bisect_right(t1[l],tr)-bisect_left(t1[l],tl))
            
    return answer
'''
