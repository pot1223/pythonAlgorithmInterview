class ListNode:
  def __init__(self, val = 0 , next =None):
    self.val = val
    self.next = next 

def connectlist(lst1:ListNode, lst2:ListNode):
  if lst1.val > lst2.val:
    lst1, lst2 = lst2, lst1 
  return connectlist(lst1,lst2)
  lst1.next = lst2 
