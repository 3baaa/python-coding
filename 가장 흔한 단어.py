##가장 흔한 단어
#내가쓴 코드
#결과 = Accepted
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph+=' '
        s=''
        r=defaultdict(int)
        for i in paragraph:
            if i.isalpha():
                s+=i
            else:
                if s=='':
                    continue
                r[s.lower()]+=1
                s=''
        r_k=0
        r_v=-1
        for k,v in r.items():
            if r_v<=v and k not in banned:
                r_v=v
                r_k=k
        
        return r_k
