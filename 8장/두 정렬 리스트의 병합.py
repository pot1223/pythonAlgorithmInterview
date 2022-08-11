# 재귀구조 풀이 

class ListNode:
  def __init__(self, val = 0 , next =None):
    self.val = val
    self.next = next 

def connectlist(lst1:ListNode, lst2:ListNode):
  if not lst1 or (lst2 and lst1.val > lst2.val):
    lst1, lst2 = lst2, lst1
  if lst1:
    lst1.next  = connectlist(lst1.next,lst2)
  return lst1

a = ListNode(1,ListNode(2,ListNode(4)))
b= ListNode(1,ListNode(3,ListNode(4)))
connectlist(a,b).next.next.next.val

  
