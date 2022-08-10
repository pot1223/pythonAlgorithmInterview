# 연결 리스트, 데크로 풀이 

from typing import Deque
import collections
from collections import deque

class ListNode:
  def __init__(self, val= 0, next = None):
    self.val = val 
    self.next = next 

def connectlstpalindrom(head:ListNode):
  lst : Deque = collections.deque() 
  if not head:
    return True
  node = head
  while node is not None:
    lst.append(node.val)
    node = node.next
  while len(lst) >1:
    if lst.popleft() != lst.pop():
      return False 
  return True   

a = ListNode(1,ListNode(2,ListNode(2,ListNode(1))))
connectlstpalindrom(a)

# 런너를 이용한 풀이 

class ListNode:
  def __init__(self, val= 0, next = None):
    self.val = val 
    self.next = next 

def connectlist_runner(head : ListNode):
  rev = None
  slow = fast = head 
  while fast and fast.next:
    fast = fast.next.next //fast 는 요소를 2개 이동 
    rev, rev.next, slow = slow, rev, slow.next  # 기존 slow 특성을 rev가 가지고 기존 rev의 특성을 rev.next가 가진 후 slow는 1개 이동 
  if fast:
    slow = slow.next # fast가 요소 끝까지 가면 slow는 해당 요소들의 정확히 반절 위치에 있기 때문에 한칸 옮겨줘야 비교가 가능하다 
  while rev and rev.val == slow.val: # rev와 slow 연결 리스트의 각 요소 비교 
    slow, rev = slow.next, rev.next
  return not rev # rev가 None이 되면 True를 출력 

a = ListNode(1,ListNode(2,ListNode(2,ListNode(1))))
connectlist_runner(a)



