##로그 파일 재정렬
#내가쓴 코드
#결과 =  Accepted
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        print(logs)
        r1=[]
        r2=[]
        for i,v in enumerate(logs):
            t=v.split()
            if t[1].isdigit():
                r2.append(v)
            else:
                r1.append(v)
        r1.sort(key=lambda x:(x.split()[1:],x.split()[0]))
        return r1+r2
