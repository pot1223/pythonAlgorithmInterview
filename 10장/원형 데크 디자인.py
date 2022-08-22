class LinkedList:
  def __init__(self, val = 0, next = None ):
    self.val = val
    self.next = next 

class MyCircularDeque:

  def __init__(self, k:int):
    self.front = LinkedList(None) # front 노드 앞에 rear 노드가 위치하게 만든다. 데크는 front 노드와 rear노드 사이에 들어간다 
    self.rear = LinkedList(None)
    self.k, self.len = k, 0  
    self.front.right, self.rear.left = self.rear, self.front
  
  def _add(self, node:LinkedList, new:LinkedList): # 노드 앞에 새로운 노드를 넣는다 
    exist = node.right
    node.right = new 
    new.left, new.right =node, exist 
    exist.left = new
  
  def _del(self, node : LinkedList): # 해당 노드 앞에 있는 노드를 삭제한다 
    exist = node.right.right
    node.right = exist
    exist.left = node 
  
  def insertFront(self, value : int): # front노드 앞에 새로운 노드를 삽입한다 
    if self.len == self.k:
      return False
    self.len += 1
    self._add(self.front, LinkedList(value))
    return True 
  
  def insertLast(self, value : int): # rear노드 뒤에 새로운 노드를 삽입한다 
    if self.len == self.k:
      return False
    self.len +=1 
    self._add(self.rear.left, LinkedList(value))
    return True

  def deleteFront(self): # front노드 앞에 있는 노드를 삭제한다 
    if self.len == 0:
      return False
    self.len -=1 
    self._del(self.front)
    return True 

  def deleteLast(self): # rear 노드 뒤에 있는 노드를 삭제한다 
    if self.len == 0:
      return False
    self.len -= 1
    self._del(self.rear.left.left)
    return True 

  def getFront(self):
    return self.front.right.val if self.len else -1 
  
  def getRear(self):
    return self.rear.left.val if self. len else -1
  
  def isEmpty(self):
    return self.len == 0
  
  def isFull(self):
    return self.len == self.k
