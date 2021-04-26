##유효한 팰린드롬
#내가쓴 코드
#결과 = Accepted
class Solution(object):
    def isPalindrome(self, s):
        s=s.upper()
        r=''
        for i in s:
            if 'A'<=i<='Z' or '0'<=i<='9':
                r+=i
        return r==r[::-1]
