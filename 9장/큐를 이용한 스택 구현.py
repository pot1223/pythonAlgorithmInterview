
import collections
class Mystack:
  def __init__(self):
    self.lst = collections.deque() # 데큐 사용 
  def push(self, x : int):
    self.x =x 
    self.lst.append(x)
  def top(self):
    return self.lst[0]
  def pop(self):
    result = self.lst.popleft()
    return result 
  def empty(self):
    if self.lst:
      return True
    else:
      return False
  
a= Mystack()
a.push(4)
