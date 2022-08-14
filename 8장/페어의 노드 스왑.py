# 값만 바꾸기 (좋은 풀이는 아니다) 

class LinkedList:
  def __init__(self, val = 0 , next = None):
    self.val = val 
    self.next = next 

def swipe(node : LinkedList):
  head = node # head에서 변경된 노드 값은 node에서도 변경이 된다 
  while head and head.next:
    head.val, head.next.val = head.next.val, head.val
    head = head.next.next 
  return node
  

a= LinkedList(1,LinkedList(2,LinkedList(3,LinkedList(4))))
swipe(a).val


# 반복구조로 스왑 

class LinkedList:
  def __init__(self, val = 0 , next = None):
    self.val = val 
    self.next = next 

def swipe(node : LinkedList):
  root = prev = LinkedList(None)
  prev.next = node
  while node and node.next:
    b = node.next
    node.next = b.next
    b.next = node 
    prev.next = b 
    node = node.next 
    prev = prev.next.next 
  return root.next 

a= LinkedList(1,LinkedList(2,LinkedList(3,LinkedList(4))))
swipe(a).next.next.val
