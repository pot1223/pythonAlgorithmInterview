class TreeNode : 
  def __init__(self , val = 0 , left = None , right = None) :
    self.val = val 
    self.left = left
    self.right = right
class Solution : 
  longest = 0 
  def diameterOfBinaryTree(self , root : TreeNode) : 
    def dfs(node : TreeNode) :
      if not node :
        return -1 
      left = dfs(node.left)
      right = dfs(node.right)
      self.longest = max(self.longest , left + right + 2)
      return max(left , right) + 1
    dfs(root)
    return self.longest

root = TreeNode(val = 1 , left = TreeNode(val = 2 , left = TreeNode(val = 4) , right = TreeNode(val = 5)) , right = TreeNode(val = 3))
Solution.diameterOfBinaryTree(Solution , root)
