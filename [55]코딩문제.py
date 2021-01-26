##가사 검색##
'''
#내가쓴 코드#
##(오류가 나온다)##
def rb(words,t,ql,s,e,wl):
    m=(s+e)//2
    vl=len(words[m])
    v=words[m]
    if s>e:
        return -1
    elif m==wl or m+1<=wl and words[m+1][:len(t)]!=t:
        return m
    elif vl>ql or t<v[:len(t)]:
        return rb(words,t,ql,s,m-1,wl)
    else:
        return rb(words,t,ql,m+1,e,wl)
    
def lb(words,t,ql,s,e,wl):
    m=(s+e)//2
    vl=len(words[m])
    v=words[m]
    if s>e:
        return -1
    elif v==t[:len(t)] and m-1>=0 and words[m-1][:len(t)]!=t:
        return m
    elif vl>=ql or t<v[:len(t)]:
        return lb(words,t,ql,s,m-1,wl)
    else:
        return lb(words,t,ql,m+1,e,wl)
        
def solution(words, queries):
    answer = []
    words.sort(key=lambda x:(len(x),x))
    wl=len(words)-1
    for i in queries:
        i1=i.find('?')
        i2=i.rfind('?')
        ql=len(i)
        if i1+i2==ql:
            t=i
        elif i1==0:
            t=i[i2+1:]
        elif i2==len(i)-1:
            t=i[:i1]
        
        n1=rb(words,t,ql,0,wl,wl)
        n2=lb(words,t,ql,0,wl,wl)
        if n1==-1:
            answer.append(0)
        else:
            answer.append(n1-n2+1)
    
    return answer

##가사 검색##
#답#
from bisect import bisect_left,bisect_right
def count_by_range(a,left_value,right_value):
  right_index=bisect_right(a,right_value)
  left_index=bisect_left(a,left_value)
  return right_index-left_index

array=[[] for _ in range(10001)]
reversed_array=[[] for _ in range(10001)]

def solution(words,queries):
  answer=[]
  for word in words:
    array[len(word)].append(word)
    reversed_array[len(word)].append(word[::-1])
  
  for i in range(10001):
    array[i].sort()
    reversed_array[i].sort()
  
  for q in queries:
    if q[0]!='?':
      res=count_by_range(array[len(q)],q.replace('?','a'),q.replace('?','z'))
    else:
      res=count_by_range(reversed_array[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
    
    answer.append(res)
  return answer
'''