class LinkedList:
  def __init__(self, val = 0, next = None):
    self.val = val 
    self.next = next

def reverseNode( node : LinkedList):
    start = node
    reverse = None
    while start:
      next, start.next = start.next, reverse 
      reverse, start = start , next 
    return reverse 
    
def changeList( node : LinkedList): 
    lst = [] 
    while node: 
      lst.append(node.val) 
      node = node.next 
    return lst     

def returnNode(resultSum : int):
  prev : LinkedList = None
  resultStr = str(resultSum)
  for r in resultStr:
    node = LinkedList(r)
    node.next = prev
    prev = node
  return prev

def sumLinked(node1 : LinkedList, node2 : LinkedList):
    node1, node2 = reverseNode(node1), reverseNode(node2)
    lstnode1, lstnode2 = changeList(node1), changeList(node2)
    resultSum = int(''.join(str(n) for n in lstnode1)) + int(''.join(str(n) for n in lstnode2))
    return returnNode(resultSum)

a = LinkedList(2,LinkedList(4,LinkedList(3)))
b = LinkedList(5,LinkedList(6,LinkedList(4)))
sumLinked(a,b).next.next.val
