class LinkedList:
  def __init__(self, val = 0, next = None ):
    self.val = val
    self.next = next 

class MyCircularDeque:

  def __init__(self, k:int):
    self.front = LinkedList(None)
    self.rear = LinkedList(None)
    self.k, self.len = k, 0  
    self.front.right, self.rear.left = self.rear, self.front
  
  def _add(self, node:LinkedList, new:LinkedList):
    exist = node.right
    node.right = new 
    new.left, new.right =node, exist 
    exist.left = new
  
  def _del(self, node : LinkedList):
    exist = node.right.right
    node.right = exist
    exist.left = node 
  
  def insertFront(self, value : int):
    if self.len == self.k:
      return False
    self.len += 1
    self._add(self.front, LinkedList(value))
    return True 
  
  def insertLast(self, value : int):
    if self.len == self.k:
      return False
    self.len +=1 
    self._add(self.rear.left, LinkedList(value))
    return True

  def deleteFront(self):
    if self.len == 0:
      return False
    self.len -=1 
    self._del(self.front)
    return True 

  def deleteLast(self):
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
