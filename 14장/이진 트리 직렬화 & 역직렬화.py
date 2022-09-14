from collections import deque 

class TreeNode :
  def __init__(self, val = 0 , left = None , right = None) :
    self.val = val
    self.left = left
    self.right = right 
    
def serialize(root : TreeNode) :
  queue = collections.deque([root])
  result =['#']
  while queue : 
    node = queue.popleft()
    if node :
      queue.append(node.left)
      queue.append(node.right)
      result.append(str(node.val))
    else :
      return.append('#')
  return ' '.join(result)

def deserialize(int(nodes[1]))
  if data = '# #' :
    return None
  nodes = data.split()
  root = TreeNode(int(nodes[1]))
  queue = collections.deque([root])
  index = 2
  while queue :
    node = queue.popleft()
    if nodes[index] is not '#' :
      node.left = TreeNode(int(nodes[index]))
      queue.append(node.left)
    index += 1
    
    if nodes[index] is not '#' :
      node.right = TreeNode(int(nodes[index]))
      queue.append(node.right)
    index += 1
  return root 
