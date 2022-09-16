import collections

class TreeNode : 
  def __init__(self , val = 0 , left = None , right = None) :
    self.val = val 
    self.left = left 
    self.right = right 

def maxDepth(root : TreeNode) : 
  if root is None : # 노드가 아무것도 없으면 0을 반환 
    return 0
  queue = collections.deque([root]) # 트리노드 객체를 리스트로 변환한 후 데크 객체 생성 
  depth = 0 
  while queue : 
    depth += 1 
    for _ in range(len(queue)) : # 루트 노드 개수만큼 
      cur_root = queue.popleft() # 루트 노드를 pop 
      if cur_root.left : # pop된 노드의 왼쪽 자식 노드가 있으면 
        queue.append(cur_root.left) # 데크에 추가 
      if cur_root.right : 
        queue.append(cur_root.right)
  return depth

tree = TreeNode(val =  3 , left = TreeNode(val = 9) , right = TreeNode(val = 20 , left = TreeNode(val = 15) , right = TreeNode(val =7)))
maxDepth(tree)
