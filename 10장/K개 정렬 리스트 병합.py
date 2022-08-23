import heapq

class LinkedList:
  def __init__(self,val=0,next= None):
    self.val =val
    self.next= next 

def mergeKList(lists):
  root =result = LinkedList(None)
  heap = []
  for i in range(len(lists)):
    if lists[i]:
      heapq.heappush(heap, (lists[i].val, i ,lists[i])) # (1,0, <연결리스트 type> ) 형식으로 heap에 넣어진다  
  print(heap)
  while heap:
    node = heapq.heappop(heap) # lists.val이 작은 순서대로 pop()된다. 
    #첫번째 반복시 (1, 0, <연결리스트type>), (1, 1, <연결리스트type>), (2, 2, <연결리스트type>)에서 가장 작은 val을 가진 (1,0,<연결리스트type>)이 pop 되고 
    # 두번째 반복시 [(1, 1, <연결리스트type>), (2, 2, <연결리스트type>), (4, 0, <연결리스트type>)]에서 가장 작은 val을 가진  (1, 1, <연결리스트type>)이 pop 된다 
    idx = node[1] 
    result.next = node[2] # result 노드에 heappop된 연결리스트가 연결된다, 첫 반복시 None-> 1- >4 -> 5 형태가 된다   

    result = result.next
    if result.next:
      heapq.heappush(heap, (result.next.val,idx,result.next)) # 첫 반복시(4,0,<연결리스트 type>) 형식으로 heap에 넣어진다.
  return root.next

a= [LinkedList(1,LinkedList(4,LinkedList(5))), LinkedList(1,LinkedList(3,LinkedList(4))),LinkedList(2,LinkedList(6))]
mergeKList(a).next.next.next.val  
