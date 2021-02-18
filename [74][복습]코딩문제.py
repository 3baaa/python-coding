##외벽 점검##
'''
#내가쓴 코드#
#(잘못쓴 코드)#
from itertools import combinations

def solution(n, weak, dist):
    d=[i for i in range(n)]*2
    r=[]
    result=[]
    
    for i in range(1,len(dist)):
        r.extend(list(combinations(dist,i)))

#답#
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer
'''
