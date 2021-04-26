##문자열 뒤집기
#내가쓴 코드
#결과 = Accepted

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i],s[-(i+1)]=s[-(i+1)],s[i]
