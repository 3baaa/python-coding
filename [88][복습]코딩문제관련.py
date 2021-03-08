## 트라이자료구조 1 ##
'''
class Node(object):
    def __init__(self,key,data=None):
        self.key=key
        self.data=data
        self.children={}

class Trie(object):
    def __init__(self):
        self.head=Node(key=None,data=None)

    def insert_string(self,input_string):
        cur_node = self.head
        for c in input_string:
            if c not in cur_node.children.keys():
                cur_node.children[c]=Node(key=c)
            cur_node=cur_node.children[c]
        cur_node.data=input_string
    def search(self,input_string):
        cur_node=self.head
        for c in input_string:
            if c not in cur_node.children.keys():
                return False
            else:
                cur_node = cur_node.children[c]
        if cur_node.data==input_string:
            return True
        else:
            return False
    def start_with(self,prefix):
        cur_node=self.head
        words=[]
        subtrie = None
        for c in prefix:
            if c in cur_node.children.keys():
                cur_node = cur_node.children[c]
                subtrie=cur_node
            else:
                return []
        cur_nodes=[subtrie]
        next_nodes=[]
        while True:
            for c in cur_nodes:
                if c.data!=None:
                    words+=[c.data]
                next_nodes+=list(c.children.values())
            if len(next_nodes)==0:
                break
            else:
                cur_nodes=next_nodes
                next_nodes=[]
        return words

t=Trie()
t.insert_string("abcd")
t.insert_string("abdc")
t.insert_string("acbd")
t.insert_string("abkd")
t.insert_string("abzzzz")
print(t.search('abdc'))
print(t.start_with("ab"))
'''
