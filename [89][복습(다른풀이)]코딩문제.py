'''

가사검색
내가쓴 코드(트라이 자료구조)
결과값은 나오나
정확성: 23.5
효율성: 0.0
합계: 23.5 / 100.0

from collections import deque
class Node():
    def __init__(self,s='',w='',l=0):
        self.s=s
        self.w=w
        self.l=l
        self.child={}
        
class Trie():
    def __init__(self):
        self.root_node=Node()
    
    def insert(self,s):
        cur_node=self.root_node
        for i in range(len(s)):
            if s[i] not in cur_node.child:
                if i==len(s)-1:
                    cur_node.child[s[i]]=Node(s,s[i],i+1)
                else:
                    cur_node.child[s[i]]=Node('',s[i],i+1)
            cur_node=cur_node.child[s[i]]
    def search(self,node,s,l,ii,r):
        if node.l>l or (node!=self.root_node and node.l<=len(s) and node.w!=s[node.l-1]):
            return
        if node.s!='' and node.l==l:
            r[ii]+=1
            return
        for i in node.child.values():
            self.search(i,s,l,ii,r)
            
def solution(words, queries):
    t=Trie()
    t2=Trie()
    answer=[0]*len(queries)
    for i in words:
        t.insert(i)
        t2.insert(i[::-1])
    for i,v in enumerate(queries):
        if v[0]=="?":
            v=v[::-1]
            t2.search(t2.root_node,v[:v.find("?")],len(v),i,answer)
        else:
            t.search(t.root_node,v[:v.find("?")],len(v),i,answer)
            
    return answer

#답#

class Node(object):
    def __init__(self, key):
        self.key = key
        self.remain_length = {}
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        remain_length = len(string)
        if remain_length in curr_node.remain_length:
            curr_node.remain_length[remain_length] += 1
        else:
            curr_node.remain_length[remain_length] = 1
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
            remain_length -= 1
            if remain_length in curr_node.remain_length:
                curr_node.remain_length[remain_length] += 1
            else:
                curr_node.remain_length[remain_length] = 1

    def search_count(self, string, check_length):
        curr_node = self.head
        if check_length+len(string) not in curr_node.remain_length:
            return 0
        
        for char in string:
            if char in curr_node.children:                
                curr_node = curr_node.children[char]
            else:
                return 0
        if check_length in curr_node.remain_length:
            return curr_node.remain_length[check_length]
        else:
            return 0


def solution(words, queries):
    t = Trie()
    inv_t = Trie()
    for word in words:
        t.insert(word)
        inv_t.insert(word[-1::-1])

    answer = []
    for i in range(len(queries)):
        query = queries[i]
        if query[0] == '?':
            query = query[-1::-1]
            chars = query.replace("?", "")
            check_length = len(query)-len(chars)
            answer.append(inv_t.search_count(chars, check_length))
        else:
            chars = query.replace("?", "")
            check_length = len(query) - len(chars)
            answer.append(t.search_count(chars, check_length))

    return answer
'''
