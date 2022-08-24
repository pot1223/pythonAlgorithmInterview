class LinkedList:
  def __init__(self, key = None, value = None):
    self.key =key
    self.value = value 
    self.next = None

class MyHashMap:
  def __init__(self):
    self.size =1000 # 기본 사이즈 설정 
    self.table = collections.defaultdict(LinkedList) # 각 LinkedList를 담게 될 자료형으로 collections.defaultdict를 통해 존재하지 않는 키를 조회할 경우 자동으로 디폴트를 생성하게 한다 
  
  def put(self,key : int, value: int):
    index= key % self.size # size의 개수만큼 키 값을 나눈 값을 해시값으로 한다 
    if self.table[index].value is None: # collections.defaultdict를 통해 존재하지 않는 키를 조회할 경우 빈 LinkedList를 생성하게 되어 None이 생기지 않기 때문에 value를 통해 비교한다 
      self.table[index] = LinkedList(key,value)
      return
    p = self.table[index]
    while p:
      if p.key == key: # 같은 키가 존재하면 
        p.value = value # 키의 값만 업데이트 하고 빠져나온다 
        return 
      if p.next is None:
        break
      p = p.next
  
    def get(self, key : int):
      index = key % self.size
      if self.table[intex].value is None:
        return -1
      p = self.table[index]
      while p:
        if p.key == key:
          return p.value
        p = p.next # 해싱 결과에 하나 이상의 노드가 존재하므로 p.next로 탐색하면서 일치하는 키를 찾는다 
      return -1 
    
    def remove(self, key : int):
      index = key % self.size
      if self.table[index].value is None:
        return
      p = self.table[index]
      if p.key == key:
        self.table[index] = LinkedList() if p.next is None else p.next
      prev = p 
      while p:
        if p.key == key:
          prev.next = p.next
          return
        prev, p = p, p.next 
      
