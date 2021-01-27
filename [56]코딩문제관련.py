#클레스 사용법 재숙지후#
'''
##Trie자료구조##
class Node(object):
  def __init__(self,key,data=None):
    self.key=key
    self.data=data
    self.children={}

class Trie(object):
  def __init__(self):
    self.head=Node(None)
  
  def insert(self,string):
    curr_node=self.head
    
    for char in string:
      if char not in curr_node.children:
        curr_node.children[char]=Node(char)
      curr_node=curr_node.children[char]
    
    curr_node.data=string
  
  def search(self,string):
    curr_node=self.head

    for char in string:
      if char in curr_node.children:
        curr_node=curr_node.children[char]
      else:
        return False
      
      if curr_node.data != None:
        return True
  
  def starts_with(self,prefix):
    curr_node=self.head
    result=[]
    subtrie=None

    for char in prefix:
      if char in curr_node.children:
        curr_node=curr_node.children[char]
        subtrie=curr_node
      else:
        return None
    
    queue=list(subtrie.children.values())
    
    while queue:
      curr=queue.pop(0)
      if curr.data!=None:
        result.append(curr.data)
      
      queue+=list(curr.children.values())
    
    return result
  
t=Trie()
words = ["romane", "romanus", "romulus", "ruben", 'rubens', 'ruber', 'rubicon', 'ruler']
for word in words:
  t.insert(word)

print(t.search("romulus"))
print(t.search("ruler"))
print(t.search("rulere"))
print(t.search("romunus"))
print(t.starts_with("ro"))
print(t.starts_with("rube"))
'''