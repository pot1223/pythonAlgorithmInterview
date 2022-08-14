class LinkedList:
  def __init__(self, val = 0, next = None):
    self.val = val 
    self.next = next
  
def linkOddEven(node : LinkedList):
  lst = []
  prev :LinkedList = None 
  while node:
    lst.append(node.val)
    node = node.next  
  lst2 = [lst[i] for i in range(len(lst)) if (i+1) % 2 != 0] # 홀수번째만 골랐음 
  lst3 = [lst[i] for i in range(len(lst)) if (i+1) % 2 == 0] # 짝수번째만 골랐음
  resultlst = lst2 + lst3
  for num in resultlst[::-1]:
    node2 = LinkedList(num)
    node2.next = prev 
    prev = node2 
  return prev
      
a = LinkedList(2,LinkedList(1,LinkedList(3,LinkedList(5,LinkedList(6,LinkedList(4,LinkedList(7)))))))
linkOddEven(a).next.next.val
