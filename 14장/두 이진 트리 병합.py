class TreeNode :
  def __init__(self , val = 0 , left = None , right = None) :
    self.val = val
    self.left = left
    self.right = right

def mergeTree(t1 : TreeNode , t2 : TreeNode) : 
  if t1 and t2 : 
    node = TreeNode(t1.val + t2.val)
    node.left = mergeTree(t1.left , t2.left)
    node.right = mergeTree(t1.right , t2.right)
    return node
  else :
    return t1 or t2

t1 = TreeNode( val = 1 , left = TreeNode( val = 3 , left = TreeNode( val = 5 )) , right = TreeNode( val = 2) )
t2 = TreeNode( val = 2 , left = TreeNode(val = 1 , right= TreeNode( val =4)) , right = TreeNode(val =3 , right = TreeNode(val =7)))
result = mergeTree(t1 , t2)
result.val
