# 스택 추상 자료형을 리스트로 구현 

class LinkedList:
  def __init__(self, item, next = None):
    self.item =item
    self.next = next 

class StackLinked:
  def __init__(self):
    self.last = None

  def push(self, item):
    self.last = LinkedList(item, self.last)

  def pop(self):
    item = self.last.item
    self.last = self.last.next
    return item  

a = StackLinked()
a.push(4)
a.push(7)
a.pop()
