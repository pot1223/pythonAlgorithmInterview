class LinkedList:
  def __init__(self, val=0 ,next =None):
    self.val = val 
    self.next = next

def customReverse(node : LinkedList, m: int, n : int ):
  root = start = LinkedList(None)
  root.next = node 
  for _ in range(m-1):
    start = start.next
  end = start.next 
  for _ in range(n-m):
    tmp = start.next
    start.next = end.next
    end.next = end.next.next 
    start.next.next = tmp
  return root.next 

node = LinkedList(1,LinkedList(2,LinkedList(3,LinkedList(4,LinkedList(5)))))
customReverse(node,2,4).next.val
