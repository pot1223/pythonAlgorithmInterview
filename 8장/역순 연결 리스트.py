class ListNode:
  def __init__(self, val = 0 , next = None):
    self.val = val
    self.next = next 

def reverseNode(head:ListNode):
  node, prev = head, None
  while node:
    next, node.next = node.next, prev
    prev, node = node, next 
  return prev 


node = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
