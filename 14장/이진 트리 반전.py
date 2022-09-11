import collections 

class TreeNode : 
  def __init__(self , val = 0 , left = None , right = None) :
    self.val = val
    self.left = left
    self.right = right

def invertTree(root : TreeNode) :
  queue = collections.deque([root])
  while queue : 
    node = queue.popleft()
    if node : 
      node.left , node.right = node.right , node.left
      queue.append(node.left)
      queue.append(node.right)
  return root 

root = TreeNode(val = 4 , left = TreeNode(val = 2 , left = TreeNode(val = 1) , right = TreeNode(val = 3)) , right = TreeNode(val = 7 , left = TreeNode(val = 6) , right = TreeNode(val = 9)))
