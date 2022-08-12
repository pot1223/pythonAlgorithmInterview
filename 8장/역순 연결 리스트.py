class ListNode:
  def __init__(self, val = 0 , next = None):
    self.val = val
    self.next = next 

def reverseNode(node:ListNode):
  start = node
  reverse = None
  while start:
    next, start.next = start.next, reverse
    reverse , start = start, next   
  return reverse 
      
node = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
reverseNode(node).val
